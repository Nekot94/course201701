import random
class RobotCharacter:
	def __init__(self,hp,damage,name):
		self.hp = hp
		self.damage = damage
		self.name = name

class RobotDexterous(RobotCharacter):
	def attack(self,victim):
		a = random.randint(1,2)
		if a == 2:
			self.damage *= 2
			print("Вау ",self.name," нанес два удара!!!")
			victim.hp -= self.damage
			print("{0.name} нанёс {1.name} {0.damage} урона".format(self,victim))
			self.damage /= 2
		if a == 1:
			self.damage = self.damage
			victim.hp -= self.damage
			print("{0.name} нанёс {1.name} {0.damage} урона".format(self,victim))

		

class RobotSurvivable(RobotCharacter):
	def attack(self,victim):
		victim.hp -= self.damage
		print("{0.name} нанёс {1.name} {0.damage} урона".format(self,victim))

class RobotStrong(RobotCharacter):
	def attack(self,victim):
		victim.hp -= self.damage
		print("{0.name} нанёс {1.name} {0.damage} урона".format(self,victim))

print("Привет вы на работ PVP!!!")
name1 = input("Первый игрок введи свое имя!!!")
print("Для начала "+name1+" выбери для себя  робота!!!\n1.Ловкий робот!Он с шансом 50% наносит два удара!!!\n2.Живучий робот!У него жизней на 50% больше чем у обычного!!!\n3.Робот силач!У этого робота атака на 50% больше чем у обычного!!!")
a = int(input())
if a == 1:
	player1 = RobotDexterous(1000,50,name1)
elif a == 2:
	player1 = RobotSurvivable(1500,50,name1)
elif a == 3:
	player1 = RobotStrong(1000,75,name1)

name2 = input("Второй игрок введи свое имя!!!")
print("Теперь "+name2+ " выбери для себя  робота!!!\n1.Ловкий робот!Он с шансом 50% наносит два удара!!!\n2.Живучий робот!У него жизней на 50% больше чем у обычного!!!\n3.Робот силач!У этого робота атака на 50% больше чем у обычного!!!")
d = int(input())
if d == 1:
	player2 = RobotDexterous(1000,50,name2)
elif d == 2:
	player2 = RobotSurvivable(1500,50,name2)
elif d == 3:
	player2 = RobotStrong(1000,75,name2)

while True:
	player1.attack(player2)
	player2.attack(player1)
	print("У "+name1+ " осталось",player1.hp)
	print("У "+name2+ " осталось",player2.hp)
	input("Нажмите Enter для продолжения!!!")
	if player1.hp <= 0:
		print("Первый игрок проиграл(((!!!Но второй победил)))")
		break
	elif player2.hp <= 0:
		print("Второй игрок проиграл(((!!!Но первый победил)))")
		break
	elif player1.hp <= 0 and player2.hp <= 0:
		print("Никто не выиграл!!!")