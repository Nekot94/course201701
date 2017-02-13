class Weapon:
	def __init__(self, name, damage, count):
		self.name = name
		self.count = count
		self.damage = damage

class Char:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def attack(self, target):
		target.hp -= self.damage
		print("{0.name} ударил {1.name} и нанес {0.damage}".format(
			self, target))

class Zombie(Char):
	pass

class Player(Char):
	def __init__(self, name, hp, damage, weapon):
		super().__init__(name, hp, damage)
		self.weapon = weapon

	def attack(self, target):
		dmg = self.damage + self.weapon.damage
		target.hp -= dmg
		print("{0.name} ударил {1.name} и нанес {2}".format(
			self, target, dmg))
		self.weapon.count -= 1

class Game():
	def start():
		player = Player("Залик", 1000, 50, Weapon("АК-47", 20, 30))
		livingdead = Zombie("Зомби-обычный", 300, 20)
		count = 0
		while True:
			player.attack(livingdead)
			livingdead.attack(player)
			input()
			if player.hp <= 0:
				print("Вы умерли и заработали {0} очков".format(count))
				break
			if livingdead.hp <= 0:
				livingdead = Zombie("Зомби-обычный", 300, 20)
				count += 1

Game.start()