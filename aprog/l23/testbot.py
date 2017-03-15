from telebot import TeleBot, types
from time import sleep
from random import choice

TOKEN = "305869982:AAEzCXecBlwuKOLR66LTb-MI0k099zk7O-o"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["ucila","kadika"])
def do_something(message):
	bot.send_message(message.chat.id, "танцую на 26 шафл")

@bot.message_handler(regexp="Амин")
def do_something(message):
	i = 0
	while True:
		i += 1
		bot.send_message(message.chat.id, "Амин " * i)
		sleep(1)

@bot.message_handler(commands=["zizn"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Ты кто ваще", url="http://uci.ru")
    keyboard.add(url_button)
    my_button = types.InlineKeyboardButton(text="че-то там", callback_data="dead")
    keyboard.add(my_button)
    bot.send_message(message.chat.id, "Нажми как братн.", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def do_callback(call):
	if call.data == "dead":
		mess = choice(["ты умер", "ты молодец", "ты сдох"])
		bot.send_message(call.message.chat.id, mess)
		bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=mess)



@bot.message_handler(func=lambda message: True)
def say_hello(message):
	if message.text.lower() == "привет":
		bot.send_message(message.chat.id, "Че за привет уци")
	else:
		bot.reply_to(message, "Cалам вац")


if __name__ == '__main__':
	bot.polling()



