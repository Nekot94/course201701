# a = 1
# arsen = "хороший пацан"
# while arsen != "лох":
# 	print("Арсен", arsen)
# 	a += 1
# 	if a == 6:
# 		arsen = "лох"

# while True:
# 	name = input("Введите имя:")
# 	if name == "Арсен":
# 		continue
# 	print(name + " красавчик")
# 	if name == "Магомед":
# 		break

names = "Магомед","Саид","Багомед"
for name in names:
	print(name)

user = {"Имя":"Абдурахман","Фамилия":"Гусейнов","Возраст":11}
for elemen in user.keys():
	print(elemen,"-",user[elemen])

for elemen in user.values():
	print(elemen)

for key, value in user.items():
	print(key, "Ж", value)
