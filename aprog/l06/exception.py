# while True:
# 	try:
# 		n1 = int(input("Введите первое число"))
# 		n2 = int(input("Введите второе число"))
# 		print("Результат деления", n1 / n2)
# 		break
# 	except ValueError:
# 		print("Ты больной идиот. Введи число!!!")
# 	except ZeroDivisionError:
# 		print ("На нуль делить нельзя!!!")
	# except:
	# 	pass

# raise ValueError

class ArslanError(Exception):
	pass
try:

	name = input ("Введите имя: ")
	if name == "Арслан":
		raise ArslanError
	else:
		print("Ты молодец")
except ArslanError:
	print("Вы ввели запрещенное имя!!!!\n\
Ваш windows будет удален через 3 секунды!!!!")

