import random
def create_player(player):
	player["Имя"] = input("Введите имя игрока: ")
	player["Жизни"] = 100
	player["Атака"] = 3
	bonus = input("добавить жизни (1), добавить атаку (2) ")
	if bonus == "1":
		player["Жизни"] += 100
	else:
		player["Атака"] += 3

def hit(agressor,victim):
	damage = agressor["Атака"] + random.randint(-3,3)
	victim["Жизни"] -= damage
	print("{0} нанес {1} урона {2}".format(agressor["Имя"],damage,victim["Имя"]))

def show_params(player):
	print("Жизни {0[Имя]} - {0[Жизни]}".format(player))


def fight(player1,player2):
	while True:
		hit(player1,player2)
		hit(player2,player1)
		show_params(player1)
		show_params(player2)
		if player1 ["Жизни"] <= 0:
			print(player2["Имя"], "убил",player1["Имя"])
			break
		if player2 ["Жизни"] <= 0:
			print(player1["Имя"], "убил",player2["Имя"])
			break
		input()


player1 = {}
player2 = {}
create_player(player1)
create_player(player2)

fight(player1,player2)






		 

