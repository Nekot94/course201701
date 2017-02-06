import random

def get_card(player):
	while True:
		yield player["Колода"].pop()

def step(player1, player2):
	k = 0
	for card1, card2 in zip(get_card(player1),get_card(player2)):
		k += 2
		print(card1, card2)
		if card1[1] > card2[1]:
			player1["Счет"] += k
			break
		elif card2[1] > card1[1]:
			player2["Счет"] += k
			break


print("     ПЬЯНИЦА    ")
suit = ["Пики","Червы","Крести","Бубны"]
deck = [(s, num) for s in suit for num in range(6,15)]
random.shuffle(deck)
# print(deck)
player1, player2 = {}, {}
player1["Колода"] = deck[:len(deck) // 2]
player2["Колода"] = deck[len(deck) // 2:]
player1["Счет"] = 0
player2["Счет"] = 0
print(player1,player2)

while player1["Колода"] and player2["Колода"]:
	step(player1,player2)
	print(player1["Счет"],player2["Счет"])
	input()


