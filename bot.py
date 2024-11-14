import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6387632922:AAFHZLAxufgGRByVOxpb2FEhJNhhwcKakj8')

game_active = False
number = None
max_attempts = 3
attempts = 0
active_player_id = None  

@bot.message_handler(commands=['ارقام', 'start', 'num'])
def start(message):
    global game_active, attempts, active_player_id
    game_active = False
    attempts = 0
    active_player_id = None

    username = message.from_user.username if message.from_user.username else "لا يوجد اسم مستخدم"

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("ابدأ اللعبة", callback_data="start_game"))

    # إرسال الصورة مع النص
    bot.send_photo(message.chat.id, "https://t.me/VIPABH/1168", caption=f"[{message.from_user.first_name}](https://t.me/{username}) حياك الله! اضغط على الزر لبدء اللعبة.", parse_mode="Markdown")

    # إرسال الرسالة مع الزر
    bot.send_message(
        message.chat.id,
        f'اهلاً [{message.from_user.first_name}](https://t.me/{username}) حياك الله! اضغط على الزر لبدء اللعبة.',
        parse_mode='Markdown', 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "start_game")
def start_game(call):
    global game_active, number, attempts, active_player_id
    if not game_active:
        number = random.randint(1, 10)
        active_player_id = call.from_user.id
        bot.send_message(call.message.chat.id, 'اختر أي رقم من 1 إلى 10 🌚 ')
        game_active = True
        attempts = 0
    else:
        bot.reply_to(call.message.chat.id, 'اللعبة قيد التشغيل، يرجى انتهاء الجولة الحالية أولاً.')

@bot.message_handler(func=lambda message: game_active and message.from_user.id == active_player_id)
def handle_guess(message):
    global game_active, number, attempts
    try:
        guess = int(message.text)
        attempts += 1

        if guess == number:
            bot.reply_to(message, "مُبارك فزتها بفخر 🥳")
            won = "https://t.me/VIPABH/2"
            bot.send_voice(message.chat.id, won)
            game_active = False
        elif attempts >= max_attempts:
            bot.reply_to(message, f"للأسف، لقد نفدت محاولاتك. الرقم الصحيح هو {number}.🌚")
       
