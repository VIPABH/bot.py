import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6387632922:AAFHZLAxufgGRByVOxpb2FEhJNhhwcKakj8')  # تأكد من إدخال مفتاح API صحيح

# المتغيرات العامة
game_active = False
number = None
max_attempts = 3
attempts = 0
active_player_id = None  # متغير لتحديد اللاعب النشط

# دالة بدء اللعبة وإعادة تعيين المتغيرات
@bot.message_handler(commands=['ارقام', 'start', 'num'])
def start(message):
    global game_active, attempts, active_player_id
    game_active = False
    attempts = 0
    active_player_id = None

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("ابدأ اللعبة", callback_data="start_game"))
    bot.send_message(message.chat.id, 'اهلاً حياك الله! اضغط على الزر لبدء اللعبة.', reply_markup=markup)

# دالة التحكم عند الضغط على زر "ابدأ اللعبة"
@bot.callback_query_handler(func=lambda call: call.data == "start_game")
def start_game(call):
    global game_active, number, attempts, active_player_id
    if not game_active:
        number = random.randint(1, 10)
        active_player_id = call.from_user.id  # تخزين ID اللاعب الذي بدأ اللعبة
        bot.send_message(call.message.chat.id, 'اختر أي رقم من 1 إلى 10 🌚 ')
        game_active = True
        attempts = 0
    else:
        bot.send_message(call.message.chat.id, 'اللعبة قيد التشغيل، يرجى انتهاء الجولة الحالية أولاً.')

# دالة التعامل مع محاولات التخمين
@bot.message_handler(func=lambda message: game_active and message.from_user.id == active_player_id)
def handle_guess(message):
    global game_active, number, attempts
    try:
        guess = int(message.text)
        attempts += 1

        if guess == number:
            bot.reply_to(message, "مُبارك فزتها بفخر 🥳")
            video_url = "https://t.me/VIPABH/2"
            bot.send_message(message.chat.id, video_url)
            game_active = False
        elif attempts >= max_attempts:
            bot.reply_to(message, f"للأسف، لقد نفدت محاولاتك. الرقم الصحيح هو {number}.🌚")
            video_url = "https://t.me/VIPABH/23"
            bot.send_message(message.chat.id, video_url)
            game_active = False
        else:
            bot.reply_to(message, "جرب مرة لخ، الرقم غلط💔")
    except ValueError:
        bot.reply_to(message, "يرجى إدخال رقم صحيح")

# تشغيل البوت مع إعادة المحاولة في حال حدوث خطأ
while True:
    try:
        bot.polling(none_stop=True)  # إضافة none_stop=True لتجنب توقف البوت
    except Exception as e:
        print(f"حدث خطأ: {e}")
