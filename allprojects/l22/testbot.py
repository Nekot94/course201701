from telebot import TeleBot, types
from time import sleep
from random import choice



TOKEN = "353796388:AAFq8Xc7tFzRSzHCLKVQZXbb9yPZLUuxIyY"

WORDS = [' лох', ' лохун', ' жук', ' идиот', ' Киса'  ]

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def never(message):
    bot.send_message(message.chat.id, "Я не начну никогда!!!")

@bot.message_handler(commands=['loh'])
def never(message):
    bot.send_message(message.chat.id, "'Это ты!!!")


@bot.message_handler(commands=['google'])
def to_google(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="В гугл", url="https://google.com")
    keyboard.add(url_button)
    my_button = types.InlineKeyboardButton(text="Конец", callback_data="end")
    keyboard.add(my_button)
    bot.send_message(message.chat.id,
     "Лох, иди в гугл.", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def do_nothing(call):
    if call.data == "end":
        bot.send_message(call.message.chat.id, "Конец!")

@bot.message_handler(regexp="Арсен")
def never(message):
    i = 0
    while True:
        i += 1
        bot.send_message(message.chat.id, "Арсен ушел" * i)
        sleep(1)







@bot.message_handler(func=lambda message: True)
def say_loh(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Ты черт")
    else:
        word = choice(WORDS)
        bot.reply_to(message, message.text + word)

if __name__ == "__main__":
    bot.polling()

