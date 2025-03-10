import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()

BOT_KEY = os.getenv("BOT_KEY")
ADMIN = os.getenv("admin")
admins = [int(admin) for admin in ADMIN.split(',')]

bot = telebot.TeleBot(BOT_KEY)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,'Hello!')

def start(admin):
    for admin in admins:
        bot.send_message(admin,'Bot started!')
@bot.message_handler(commands=['buttons'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Button1')
    button2 = types.KeyboardButton('/start')
    markup.add(button1,button2)

    bot.send_message(message.chat.id,"Choose option:",reply_markup=markup)


@bot.message_handler(commands=['inline'])
def inline_buttons(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton('Image',callback_data="image")
    button2 = types.InlineKeyboardButton('Video',callback_data="video")
    markup.add(button1,button2)

    bot.send_message(message.chat.id,"Choose option:",reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def callback_function(call):
    if call.data == 'image':
        with open("image.jpg",'rb') as image:
            bot.send_photo(call.message.chat.id,image)
        bot.answer_callback_query(call.id,"Your receive image")
    else:
        with open("video.mp4",'rb') as video:
            bot.send_video(call.message.chat.id,video)
        bot.answer_callback_query(call.id,"Your receive video")



if __name__ =='__main__':
    start(admins)
    bot.polling(non_stop=True)
