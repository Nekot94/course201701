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

	def add_friend(self,*args):
		ins = "INSERT OR REPLACE INTO answers VALUES (?,?,?,?,?)"
		self.curs.execute(ins,args)
		self.conn.commit()




	def create_tables(self):
		# self.curs.execute("DROP TABLE questions")
		# self.curs.execute("DROP TABLE answers")
		self.curs.execute(""" CREATE TABLE IF NOT EXISTS questions
		(type VARCHAR(50) PRIMARY KEY,
		question VARCHAR(250)
		)""")
		self.give_questions()
		rows = self.curs.execute("SELECT * FROM questions")
		# print(rows.fetchall())
		crt =  "CREATE TABLE IF NOT EXISTS answers (name VARCHAR(50) PRIMARY KEY," 
		for row in rows:
			crt += "{0} VARCHAR(200),".format(row[0])
		crt = crt[:-1] + ")"
		print(crt)
		self.curs.execute(crt)

		self.add_friend("Леха","Фамилия","100","нет","да")

		rows = self.curs.execute("SELECT * FROM answers")
		for row in rows:
			print(row)

	def ask_questions(self,name):
		rows = self.curs.execute("SELECT * FROM questions")
		print("У мнея так брата звали")
		answers = []
		for row in rows:
			answ =input(row[1])
			answers.append(answ)

		self.add_friend(name,*answers)


	def give_names(self,name):
		rows = self.curs.execute("SELECT name FROM answers")
		# print(rows.fetchall())
		names = [row[0] for row in rows]
		# print(names)
		return name in names

	def about_you(self,name):
		row = self.curs.execute("SELECT * FROM answers WHERE name = ?", (name,))
		row = row.fetchone()
		print("Я тебя где-то видел, твоя фамилия {0[1]} \n Ты выглядишь моложе меня, хотя тебе аж {0[2]} \n Твой ответ на причинение боли был {0[3]} \n Твой ответ на покупку семечек был {0[4]}".format(row))



	def start_chat(self):
		name = input("Как мать назвала? А меня зовут {0.name} ".format(self))
		if self.give_names(name):
			self.about_you(name)
		else:
			self.ask_questions(name)



bot = Chatbot("Колян")
bot.create_tables()
bot.start_chat()
