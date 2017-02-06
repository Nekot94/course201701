from random import randint, shuffle

def get_card(player):
	while True:
		yield player["Колода"].pop()


def turn(player1, player2):
	k = 0
	for card1, card2 in zip(get_card(player1), get_card(player2)):
		k += 2
		print(card1 , card2)
		if card1[1] > card2[1]:
			player1["Счет"] += k
			break
		elif card1[1] < card2[1]:
			player2["Счет"] += k
			break
		else:
			print("Совпали")


def coloda():
	masti = ['Червы', 'Пики', 'Крести', 'Бубны' ]
	deck = [(i, j) for i in masti for j in range(2,16)]
	return deck

deck = coloda()

shuffle(deck)
player1 = {}
player2 = {}
player1["Колода"] = deck[:len(deck) // 2]
player2["Колода"] = deck[len(deck) // 2:]

# print(player1, "----",player2)
player1["Счет"] = 0
player2["Счет"] = 0

while True:
	turn(player1, player2)
	print(player1["Счет"], player2["Счет"])
	input()
	if not player1["Колода"] or not player2["Колода"]:
		break

