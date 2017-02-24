import sqlite3
from collections import OrderedDict

QUESTIONS = OrderedDict({
	"surname": "Как тебя дразнили?",
	"age": "Сколько лет уже страдаешь?",
	"pain": "Ты любишь причинять боль?",
	"quest": "Купишь мне семечки?"
	})


class Chatbot:
	
	def __init__(self, name):
		self.conn = sqlite3.connect('bot_db.db')
		self.curs = self.conn.cursor()
		self.name = name
	
	def __del__(self):
		self.curs.close()
		self.conn.close()

	def give_questions(self):
		ins = "INSERT OR REPLACE INTO questions (type, question) VALUES(?,?)"
		for key, value in QUESTIONS.items():
			self.curs.execute(ins,(key, value))
		self.conn.commit()


	def create_tables(self):
		self.curs.execute(""" CREATE TABLE IF NOT EXISTS questions
		(type VARCHAR(50),
		question VARCHAR(250)
		)""")
		self.give_questions()
		rows = self.curs.execute("SELECT * FROM questions")
		for row in rows:
			print(row) 


	def start_chat(self):
		name = input("Как мать назвала? А меня зовут {0.name} ".format(self))
		# if name in self.give_names():
		# 	self.about_you(name)
		# else:
		# 	self.ask_questions()



bot = Chatbot("Колян")
bot.create_tables()
bot.start_chat()
