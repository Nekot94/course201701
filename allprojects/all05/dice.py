import random
player1 = {"Деньги":1000,"Ставка":0}
player2 = {"Деньги":1000,"Ставка":0}
player1["Имя"] = input("Введите имя 1-го игрока: ")
player2["Имя"] = input("Введите имя 2-го игрока: ")

while True:
	player1["Ставка"] = int(input(player1["Имя"] + " введите ставку: "))
	if player1["Ставка"] >= player1["Деньги"]:
		player1["Ставка"] = player1["Деньги"]

	player2["Ставка"] = int(input(player2["Имя"] + " введите ставку: "))
	if player2["Ставка"] >= player2["Деньги"]:
		player2["Ставка"] = player2["Деньги"]

	player1["Бросок"] = random.randint(2,12)
	player2["Бросок"] = random.randint(2,12)
	if player1["Бросок"] > player2["Бросок"]:
		print(player1["Имя"]," победил")
		player1["Деньги"] += player2["Ставка"]
		player2["Деньги"] -= player2["Ставка"]
	elif player2["Бросок"] > player1["Бросок"]:
		print(player2["Имя"]," победил")
		player2["Деньги"] += player1["Ставка"]
		player1["Деньги"] -= player1["Ставка"]
	else:
		print("Ничья")

	print(player1["Имя"],player1["Деньги"])
	print(player2["Имя"],player2["Деньги"])

	if player1["Деньги"] <= 0:
		print(player2["Имя"], "разгромил",player1["Имя"])
		break
	if player2["Деньги"] <= 0:
		print(player1["Имя"], "разгромил",player2["Имя"])
		break