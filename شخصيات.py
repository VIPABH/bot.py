import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("6387632922:AAFHZLAxufgGRByVOxpb2FEhJNhhwcKakj8")  # استبدل YOUR_BOT_TOKEN برمز التوكن الخاص بك

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
