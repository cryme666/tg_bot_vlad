import os
from dotenv import load_dotenv
import telebot

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


if __name__ =='__main__':
    bot.polling(non_stop=True)
    start(admins)
