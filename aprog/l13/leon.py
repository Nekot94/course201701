import random
fighter1 = {"Имя":"Джон","Деньги":1000,"Ставка":0,"Удар":0}
fighter2 = {"Имя":"Джон","Деньги":1000,"Ставка":0,"Удар":0}

fighter1["Имя"] = input("Введите ваше имя:\n")
fighter2["Имя"] = input("Введите ваше имя:\n")

while True:
	fighter1["Ставка"] = int(input(fighter1["Имя"] + "," + "введите сумму, которую вы хотите поставить на своего бойца:\n"))
	if fighter1["Ставка"] > fighter1["Деньги"] :
		fighter1["Ставка"] = fighter1["Деньги"]
	fighter2["Ставка"] = int(input(fighter2["Имя"] + "," + "введите сумму, которую вы хотите поставить на своего бойца:\n"))
	if fighter2["Ставка"] > fighter2["Деньги"] :
		fighter2["Ставка"] = fighter2["Деньги"]
	fighter1["Удар"] = random.randint(1,2)
	fighter2["Удар"] = random.randint(1,2)
	if fighter1["Удар"] > fighter2["Удар"]:
		fighter2["Ставка"] = fighter1["Ставка"]
		print("Ставки сравнялись: ",fighter1["Ставка"])
	elif fighter2["Ставка"] > fighter1["Ставка"]:
		fighter1["Ставка"] = fighter2["Ставка"]
		print("Ставки сравнялись: ",fighter2["Ставка"])
	if fighter1["Ставка"] > fighter1["Деньги"]:
		fighter1["Ставка"] = fighter1["Деньги"]
		print("Ставка: ",fighter1["Ставка"])
	elif fighter2["Ставка"] > fighter2["Деньги"]:
		fighter2["Ставка"] = fighter2["Деньги"]
		print("Ставка: ",fighter2["Ставка"])
	if fighter1["Удар"] > fighter2["Удар"]:
		fighter1["Деньги"] += fighter2["Ставка"]
		fighter2["Деньги"] -= fighter2["Ставка"]
		print(fighter1["Имя"],"Победил")
		print(fighter1["Имя"],"Имеет: ",fighter1["Деньги"])
		print(fighter2["Имя"],"Имеет: ",fighter2["Деньги"])
	elif fighter2["Удар"] > fighter1["Удар"]:
		fighter2["Деньги"] += fighter1["Ставка"]
		fighter1["Деньги"] -= fighter1["Ставка"]
		print(fighter2["Имя"],"Победил")
		print(fighter1["Имя"],"Имеет: ",fighter1["Деньги"])
		print(fighter2["Имя"],"Имеет: ",fighter2["Деньги"])
	else:
		print("Ничья")

	if fighter1["Деньги"] <= 0:
		print("Боец игрока",fighter2["Имя"],"нокаутировал бойца игрока",fighter1["Имя"])
		break
	if fighter2["Деньги"] <= 0:
		print("Боец игрока",fighter1["Имя"],"нокаутировал бойца игрока",fighter2["Имя"])
		break