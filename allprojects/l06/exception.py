while True:
	try:
		number = int(input("Введите число: "))
		print("7 /", number, 7 / number)
		break
	except ValueError:
		print("Ты идиот надо ввести число!!!")
	except ZeroDivisionError:
		print("Ты мой герой - ты делишь на ноль(Идиот)")

# raise ValueError;

class GamidError(Exception):
	pass


try:
	name = input("Введите имя: ")
	if name == "Гамид":
		raise GamidError
except GamidError:
	print("Ты ввел Гамид. Фатальная ошибка!")