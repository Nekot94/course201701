# a = 1
# name = "Амин"
# while name != "Артур":
# 	print(name)
# 	a += 1
# 	if a == 4:
# 		name = "Артур"

# while True:
# 	name = input("Угадайте нужное имя: ")
# 	if name == "Саид":
# 		print("Как ты посмел?")
# 		continue
# 	if name == "Зубер":
# 		print("Как ты догадася?!")
# 		break
# 	print("Лошарааа!!!!")

names = ["Кадыр","Амин","Аслан"]
for name in names:
	print(name)

user = {"Имя":"Амалия","Фамилия":"Рамазанова",
"Возраст":"16"}
for key in user.keys():
	print(key, "-", user[key])

for value in user.values():
	print(value)


for key, value in user.items():
	print(key, value)