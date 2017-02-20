from random import randint

class CharError(Exception):
	pass

class Potion:
	
	def __init__(self, restore, count):
		self.restore = restore
		self.count = count

class Weapon:

	def __init__(self, name, damage, block):
		self.name = name
		self.damage = damage
		self.block = block

class Char:

	def __init__(self, name, hp, mp, defense, crit, evasion, weapon, potion):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.defense = defense
		self.crit = crit
		self.evasion = evasion
		self.weapon = weapon
		self.potion = potion
	
	def __str__(self):
		return "Имя:{0.name} Жизни:{0.hp} Мана:{0.mp} Защита:{0.defense} Крит:{0.crit} Уклонение:{0.evasion} Оружие:{0.weapon.name} Зелья:{0.potion.count}".format(self)

	def attack(self, target):
		damage = ((self.weapon.damage + randint(10, 25)) - target.defense)
		critdmg = (((self.weapon.damage + randint(10, 25)) * 1.5)  - target.defense)
		
		if randint(1,100) <= target.evasion:
			print("{0} не попал по {1}".format(self.name, target.name))
		else:
			if randint(1, 100) <= target.weapon.block:
				print("{1} блокировал удар {0}".format(self.name, target.name))
			else:
				if randint(1,100) <= self.crit:
					target.hp -= critdmg
					print("{0} нанес крит. урон {1} в размере {2} ".format(self.name, target.name, critdmg))
				else:
					target.hp -= damage
					print("{0} нанес {1} {2} урона".format(self.name, target.name, damage))


class Warrior(Char):

	def cast(self, target):
		self.mp -= 100
		target.hp -= 150
		print("{0.name} замахнулся оружием но ударил {1.name} ногой между ног нанося 150 урона".format(self, target))

class Archer(Char):

	def cast(self, target):
		self.mp -= 100
		target.hp -= 150
		print("{0.name} точно прицелился и кинул в {1.name} {0.weapon.name} нанося 150 урона".format(self, target))

class Mage(Char):

	def cast(self, target):
		self.mp -= 100
		target.hp -= 200
		print("{0.name} заставил {1.name} поверить что у него на 150 меньше жизней".format(self, target))

class Game:
	
	def start():
		while True:
			try:
				name = input("Введите Имя первого игрока: ") 
				if len(name) > 20:
					raise CharError
				else:
					break
			except CharError:
				print("Введите не более 20 символов ")		
		
		while True:
			try:	
				race = input("Выберите расу для первого Игрока : Человек (1) : Орк (2) : Эльф (3) ")
				if race == "1" or race == "2" or race == "3":
					break
				else:
					raise CharError
			except CharError:
				print("Выберите расу ")

		while True:
			try:
				klass = input("выберите класс : Воин (1) : Лучник (2) : Маг (3) ")
				if race == "1" or race == "2" or race == "3":
					break
				else:
					raise CharError
			except CharError:
				print("Выберите класс ")
		
		if race == "1" and klass == "1": #ЕСЛИ ВЫБРАН ЧЕЛОВЕК И ВОИН
			weapon = input("Выберите оружие : Двуручный меч (1) : Меч и Щит (2) ")
			if weapon == "1": 
				player1 = Warrior(name, 2000, 500, 40, 10, 5, Weapon("Двуручный меч", 110, 5), Potion(500, 5))
			else:
				player1 = Warrior(name, 2000, 500, 40, 10, 5, Weapon("Меч и Щит", 90, 25), Potion(500, 5))

		if race == "1" and klass == "2": #ЕСЛИ ВЫБРАН ЧЕЛОВЕК И ЛУЧНИК
			weapon = input("Выберите оружие : Лук (1) : Арбалет (2) ")
			if weapon == "1": 
				player1 = Archer(name, 2000, 500, 40, 20, 15, Weapon("Лук", 110, 0), Potion(500, 5))
			else:
				player1 = Archer(name, 2000, 500, 40, 25, 10, Weapon("Арбалет", 110, 0), Potion(500, 5))

		if race == "1" and klass == "3": #ЕСЛИ ВЫБРАН ЧЕЛОВЕК И МАГ
			weapon = input("Выберите оружие : Посох (1) : Жезл (2) ")
			if weapon == "1": 
				player1 = Mage(name, 2000, 700, 40, 10, 0, Weapon("Посох", 90, 5), Potion(500, 5))
			else:
				player1 = Mage(name, 2000, 700, 40, 10, 0, Weapon("Жезл", 110, 0), Potion(500, 5))

		if race == "2" and klass == "1": #ЕСЛИ ВЫБРАН ОРК И ВОИН
			weapon = input("Выберите оружие : Огромный Топор (1) : Двуручная Булава (2) ")
			if weapon == "1": 
				player1 = Warrior(name, 2100, 300, 45, 15, 0, Weapon("Огромный Топор", 125, 5), Potion(500, 5))
			else:
				player1 = Warrior(name, 2100, 300, 45, 15, 0, Weapon("Двуручная Булава", 120, 5), Potion(500, 5))

		if race == "2" and klass == "2": #ЕСЛИ ВЫБРАН ОРК И ЛУЧНИК
			weapon = input("Выберите оружие : Камень (1) : Зига (2) ")
			if weapon == "1": 
				player1 = Archer(name, 2100, 300, 45, 15, 0, Weapon("Камень", 100, 0), Potion(500, 5))
			else:
				player1 = Archer(name, 2100, 300, 45, 15, 0, Weapon("Зигу", 115, 5), Potion(500, 5))

		if race == "2" and klass == "3": #ЕСЛИ ВЫБРАН ОРК И МАГ
			weapon = input("Выберите оружие : Руки (1) : Самовнушение (2) ")
			if weapon == "1": 
				player1 = Mage(name, 2100, 500, 45, 10, 0, Weapon("Руки", 90, 5), Potion(500, 5))
			else:
				player1 = Mage(name, 2100, 500, 45, 10, 0, Weapon("Самовнушение", 85, 10), Potion(500, 5))

		if race == "3" and klass == "1": #ЕСЛИ ВЫБРАН ЭЛЬФ И ВОИН
			weapon = input("Выберите оружие : Кинжал (1) : Длинный Меч (2) ")
			if weapon == "1": 
				player1 = Warrior(name, 1900, 600, 35, 15, 15, Weapon("Кинжал ", 90, 5), Potion(500, 5))
			else:
				player1 = Warrior(name, 1900, 600, 35, 15, 10, Weapon("Длинный Меч", 100, 5), Potion(500, 5))

		if race == "3" and klass == "2": #ЕСЛИ ВЫБРАН ЭЛЬФ И ЛУЧНИК
			weapon = input("Выберите оружие : Лук (1) : Арбалет (2) ")
			if weapon == "1": 
				player1 = Archer(name, 1900, 600, 35, 25, 25, Weapon("Лук", 100, 0), Potion(500, 5))
			else:
				player1 = Archer(name, 1900, 600, 35, 30, 20, Weapon("Арбалет", 115, 5), Potion(500, 5))

		if race == "3" and klass == "3": #ЕСЛИ ВЫБРАН ЭЛЬФ И МАГ
			weapon = input("Выберите оружие : Сфера (1) : Некрономикон (2) ")
			if weapon == "1": 
				player1 = Mage(name, 1900, 800, 35, 15, 15, Weapon("Сфера", 90, 0), Potion(500, 5))
			else:
				player1 = Mage(name, 1900, 800, 35, 15, 15, Weapon("Некрономикон", 85, 5), Potion(500, 5))

		while True:
			try:
				name = input("Введите Имя второго игрока: ") 
				if len(name) > 20:
					raise CharError
				else:
					break
			except CharError:
				print("Введите не более 20 символов ")		
		
		while True:
			try:	
				race = input("Выберите расу для второго Игрока : Человек (1) : Орк (2) : Эльф (3) ")
				if race == "1" or race == "2" or race == "3":
					break
				else:
					raise CharError
			except CharError:
				print("Выберите расу ")

		while True:
			try:
				klass = input("выберите класс : Воин (1) : Лучник (2) : Маг (3) ")
				if race == "1" or race == "2" or race == "3":
					break
				else:
					raise CharError
			except CharError:
				print("Выберите класс ")
		
		if race == "1" and klass == "1": #ЕСЛИ ВЫБРАН ЧЕЛОВЕК И ВОИН
			weapon = input("Выберите оружие : Двуручный меч (1) : Меч и Щит (2) ")
			if weapon == "1": 
				player2 = Warrior(name, 2000, 500, 40, 10, 5, Weapon("Двуручный меч", 110, 5), Potion(500, 5))
			else:
				player2 = Warrior(name, 2000, 500, 40, 10, 5, Weapon("Меч и Щит", 90, 25), Potion(500, 5))

		if race == "1" and klass == "2": #ЕСЛИ ВЫБРАН ЧЕЛОВЕК И ЛУЧНИК
			weapon = input("Выберите оружие : Лук (1) : Арбалет (2) ")
			if weapon == "1": 
				player2 = Archer(name, 2000, 500, 40, 20, 15, Weapon("Лук", 110, 0), Potion(500, 5))
			else:
				player2 = Archer(name, 2000, 500, 40, 25, 10, Weapon("Арбалет", 110, 0), Potion(500, 5))

		if race == "1" and klass == "3": #ЕСЛИ ВЫБРАН ЧЕЛОВЕК И МАГ
			weapon = input("Выберите оружие : Посох (1) : Жезл (2) ")
			if weapon == "1": 
				player2 = Mage(name, 2000, 700, 40, 10, 0, Weapon("Посох", 90, 15), Potion(500, 5))
			else:
				player2 = Mage(name, 2000, 700, 40, 10, 0, Weapon("Жезл", 110, 0), Potion(500, 5))

		if race == "2" and klass == "1": #ЕСЛИ ВЫБРАН ОРК И ВОИН
			weapon = input("Выберите оружие : Огромный Топор (1) : Двуручная Булава (2) ")
			if weapon == "1": 
				player2 = Warrior(name, 2100, 300, 45, 15, 0, Weapon("Огромный Топор", 125, 5), Potion(500, 5))
			else:
				player2 = Warrior(name, 2100, 300, 45, 15, 0, Weapon("Двуручная Булава", 120, 5), Potion(500, 5))

		if race == "2" and klass == "2": #ЕСЛИ ВЫБРАН ОРК И ЛУЧНИК
			weapon = input("Выберите оружие : Камень (1) : Зига (2) ")
			if weapon == "1": 
				player2 = Archer(name, 2100, 300, 45, 15, 0, Weapon("Камень", 100, 0), Potion(500, 5))
			else:
				player2 = Archer(name, 2100, 300, 45, 15, 0, Weapon("Зигу", 115, 5), Potion(500, 5))

		if race == "2" and klass == "3": #ЕСЛИ ВЫБРАН ОРК И МАГ
			weapon = input("Выберите оружие : Руки (1) : Самовнушение (2)")
			if weapon == "1": 
				player2 = Mage(name, 2100, 500, 45, 10, 0, Weapon("Руки", 90, 15), Potion(500, 5))
			else:
				player2 = Mage(name, 2100, 500, 45, 10, 0, Weapon("Самовнушение", 85, 15), Potion(500, 5))

		if race == "3" and klass == "1": #ЕСЛИ ВЫБРАН ЭЛЬФ И ВОИН
			weapon = input("Выберите оружие : Кинжал (1) : Длинный Меч (2) ")
			if weapon == "1": 
				player2 = Warrior(name, 1900, 600, 35, 15, 15, Weapon("Кинжал ", 90, 5), Potion(500, 5))
			else:
				player2 = Warrior(name, 1900, 600, 35, 15, 10, Weapon("Длинный Меч", 100, 5), Potion(500, 5))

		if race == "3" and klass == "2": #ЕСЛИ ВЫБРАН ЭЛЬФ И ЛУЧНИК
			weapon = input("Выберите оружие : Лук (1) : Арбалет (2) ")
			if weapon == "1": 
				player2 = Archer(name, 1900, 600, 35, 25, 25, Weapon("Лук", 100, 0), Potion(500, 5))
			else:
				player2 = Archer(name, 1900, 600, 35, 30, 20, Weapon("Арбалет", 115, 5), Potion(500, 5))

		if race == "3" and klass == "3": #ЕСЛИ ВЫБРАН ЭЛЬФ И МАГ
			weapon = input("Выберите оружие : Сфера (1) : Некрономикон (2) ")
			if weapon == "1": 
				player2 = Mage(name, 1900, 800, 35, 15, 15, Weapon("Сфера", 90, 0), Potion(500, 5))
			else:
				player2 = Mage(name, 1900, 800, 35, 15, 15, Weapon("Некрономикон", 85, 5), Potion(500, 5))

		print(player1)
		print(player2)
		turn = 1

		while True:
			input()
			print("Текущий Ход : {0}".format(turn))
			print("{0.name} : Кол-во HP : {0.hp} Кол-во MP : {0.mp} Кол-во Зелий : {0.potion.count}".format(player1))
			print("{0.name} : Кол-во HP : {0.hp} Кол-во MP : {0.mp} Кол-во Зелий : {0.potion.count}".format(player2))
			
			if randint(1, 100) <= 20 and player1.mp >= 100:
				player1.cast(player2)
			else:
				player1.attack(player2)

			if randint(1, 100) <= 20 and player2.mp >= 100:
				player2.cast(player1)
			else:
				player2.attack(player1)

			if player1.hp <= 0:
				if player1.potion.count > 0:
					player1.hp += player1.potion.restore
					print("{0} Использовал Зелье".format(player1.name))
					player1.potion.count -= 1
				else:
					print(player2.name, "убил", player1.name)
					break
			if player2.hp <= 0:
				if player2.potion.count > 0:
					player2.hp += player2.potion.restore
					print("{0} Использовал Зелье".format(player2.name))
					player2.potion.count -= 1
				else:
					print(player1.name, "убил", player2.name)
					break
			turn += 1
		
Game.start()