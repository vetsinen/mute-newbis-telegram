import telebot
from time import time

bot = telebot.TeleBot('5103975817:AAGuomwjpFO2lgVxiiVBdzbUU8pcnEzPlf0')
CHANNEL_NAME = '@merengue42'

@bot.message_handler(content_types=[
    "new_chat_members"
])
def mute(message):
    print('somebody to ban', message.from_user.id)
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time()+7*86400)
    phrase = f'доброго дня, {message.from_user.first_name} {message.from_user.last_name}, дякую, що приєднались до чату спільноти. Щоб зменшити кількість спаму всі нові акаунти автоматично переводяться в режим "тільки читання". аби писати в чаті - представтесь, будь ласка, в спеціальному чаті @dance_blockpost. ваш акаунт може буде перевединий в повний режим тільки після перевірки вашої заявки адмінами.'
    bot.send_message(message.chat.id, phrase)

@bot.message_handler()
def get_text_messages(message):
    bot.send_message(message.from_user.username, "hello. how can I help you?")


bot.infinity_polling()
