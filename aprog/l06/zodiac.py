class WrongDay(Exception):
	pass
class WrongMonth(Exception):
	pass

while True:
	try:	
		date = input("Введите дату рождения в формате дд.мм.гггг: ")
		d = int(date[0:2])
		m = int(date[3:5])
		y = int(date[6:10])
		print(d, m, y)
		if  1 < d > 31:
			raise WrongDay
		if  1 < m > 12:
			raise WrongMonth

		if (m == 8 and d in range(23, 32)) or \
		(m == 9 and d in range(1, 24)):
			print("Ты дева")
		else: 
			print("Ты не дева")

		break
	except ValueError: 
		print("Введите дату в правильном формате дд.мм.гггг")
	except WrongDay:
		print("Введите правильное число ")
	except WrongMonth:
		print("Введите правильный месяц ")
