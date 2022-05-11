import telebot
from time import time
token="наш токен"

bot = telebot.TeleBot('<MY-BOT-TOKEN>')
@bot.message_handler(content_types=[
    "new_chat_members"
])
def mut(message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time()+86400)


