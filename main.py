import telebot

# توکن ربات تلگرام خود را اینجا وارد کنید
TOKEN = ''

# ایجاد یک شی ربات
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    welcome_message = "سلام، من دستیار حسام خالصی هستم \n چطوری میتونم کمکتون کنم؟"
    
    # ایجاد کیبورد شیشه‌ای برای انتخاب گزینه
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("راه های ارتباطی")
    item2 = telebot.types.KeyboardButton("درمورد من")
    item3 = telebot.types.KeyboardButton("نمونه کارها")
    markup.add(item1, item2, item3)
    
    # ارسال پیام و کیبورد به کاربر
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):

    if message.text == "راه های ارتباطی":
        bot.reply_to(message, "راه های ارتباطی : \n Gmail : info@hesamkhalesi.ir \n Website : www.hesamkhalesi.ir \n Anonymouslink(پیام مستقیم) : https://telegram.me/BiChatBot?start=sc-1111229-XHxxQvo")

    elif message.text == "نمونه کارها":
        bot.reply_to(message, "میتونی نمونه کار ها و پروژه هاشو تو کانال زیر ببینی : \n tg.me/hesam_Desighner" )
    
    elif message.text == "درمورد من": 
        bot.reply_to(message, "حسام خالصی ملقب به لورد و پدر جاوا اسکریپت شناخته میشود. \n\n گفته میشه بتمن و سوپرمن 2 تا از زیردستاش بودن و راضی هم هستن. \n پیشنهاد میکنم امتحان کنید \n برنامه نویس و کد نویسی در رگ هاش جاریه ، وقتی فعال شد من درست شدم. \n اگه میخوای بیشتر بدونی برو تو سایتش  : \n www.hesamkhalesi.ir" )

    else:
        bot.reply_to(message, "متوجه نشدم جیگر، یکی از گزینه هارو انتخاب کن")

bot.polling()
