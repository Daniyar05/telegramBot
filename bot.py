import telebot
from telebot import types
from chatGPT import get_requests
# Создание экземпляра бота
bot = telebot.TeleBot('6407443894:AAHVtuHgBldDzOoWW4UF7zpslKnSCjIXY-Y')


# Словарь для хранения состояний пользователей
user_states = {}
api_hash = ''
api_key = ''
@bot.message_handler(commands=['start'])
def start(message):

    # Отправка сообщения с инлайн кнопками
    bot.send_message(message.chat.id, "")


@bot.message_handler(func=lambda message: True)
def handle_response(message):
    print(message.text)
    result = get_requests(message.text)
    bot.send_message(message.chat.id, result)



bot.polling()