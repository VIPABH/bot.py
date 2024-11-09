import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6387632922:AAFHZLAxufgGRByVOxpb2FEhJNhhwcKakj8')

game_active = False
number = None
max_attempts = 3
attempts = 0
active_player_id = None  # متغير لتحديد اللاعب النشط

@bot.message_handler(commands=['ارقام', 'start', 'num'])
def start(message):
    global game_active, attempts, active_player_id
    game_active = False
    attempts = 0
    active_player_id = None

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("ابدأ اللعبة", callback_data="start_game"))
    bot.send_message(message.chat.id, 'اهلاً حياك الله! اضغط على الزر لبدء اللعبة.', reply_markup=markup)

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

@bot.message_handler(func=lambda message: message.text == "الشخصيات")
def send_welcome(message):
    # إنشاء قائمة الأزرار
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("ابن هاشم", callback_data="button1")
    button2 = InlineKeyboardButton("لبن", callback_data="button2")
    button3 = InlineKeyboardButton("هاكس", callback_data="button3")
    button4 = InlineKeyboardButton("ياسر الواع", callback_data="button4")
    button5 = InlineKeyboardButton("الولائي", callback_data="button5")
   
    # إضافة الأزرار إلى القائمة
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "اختر شخصية🌚:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # إرسال الصورة مع النص حسب الزر المضغوط
    if call.data == "button1":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1188", caption="مبرمج مصمم طالب مدرسي يشتغل بالعطور ويلعب جيم \n دائما مشغول لان يشتغل 33 ساعة باليوم")
    elif call.data == "button2":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1189", caption="شخص من الموصل متوحد منبوذ \n غثيث غالبا بس متواضع اكثر من ابن هاشم ")
    elif call.data == "button3":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1190", caption="هاكس \n متسلط عنصري ضد الرجال ودائما هوه حق ما يحب يتحايز للخطأ \n شخصية قيادية")
    elif call.data == "button4":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1192", caption="ياسر \n قائد قوات الشتبوست ومؤسس الجيل الذهبي \n انعرف فتره ب عداوته وي ابو علوش ومساعد")  
    elif call.data == "button5":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1191", caption="الولائي خوش شخص وبنفس الوقت مو خوش \n عنده سيارات ويحب يشارك صورهن بالكروب وهذا السبب الي يخلي العالم تشوفه غثيث \n جان اسمه محمد وصار مرتضئ راسب بالسادس 5 سنوات")

# تشغيل البوت
bot.polling()
