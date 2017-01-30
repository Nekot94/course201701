class Derror(Exception):
	pass

class Merror(Exception):
	pass

while True:
	try:
		data = input("Введи дату рождения по типу дд.мм.гггг ")
		d = int(data[0:2])
		m = int(data[3:5])
		y = int(data[6:11])
		print(d,m,y)
		
		if d > 31 or d < 1:
			raise Derror
		
		if m > 12 or m < 1:
			raise Merror
		if (d in range (22,31) and m == 6) or \
		(d in range (1,24) and m == 7):
			print("Ты рак")
		else:
			print("Ты не рак")

		break

		
	except ValueError:
		print("Вы ввели числа не по форме")
	except Derror:
		print("Вы ввели несуществующий день")

	except Merror:
		print("Вы ввели несуществующий месяц")


