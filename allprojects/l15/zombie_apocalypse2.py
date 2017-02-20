import json
import random

class Weapon:
	def __init__(self, name, damage, count, original_count):
		self.name = name
		self.damage = damage
		self.count = count
		self.original_count = original_count


class Char:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def attack(self, target):
		target.hp -= self.damage
		print("{0.name} ударил {1.name} и нанес {0.damage}".format(
			self, target))

	def show_stats(self):
		print("{0.name}, жизни: {0.hp}, урон: {0.damage}".format(self))

class Zombie(Char):
	pass

class Player(Char):
	def __init__(self, name, hp, damage, weapons):
		super().__init__(name, hp, damage)
		self.weapons = weapons

	def show_weapons(self):
		print("У вас есть:")
		for num, weapon in enumerate(self.weapons):
			print("{0}. {1.name}, урон: {1.damage}, колличество: {1.count}".format(num, weapon))

	def choose_weapon(self):
		self.damage = 0
		while True:
			try:
				weapon_num = int(input("Введите номер оружия: "))
				if weapon_num in range(len(self.weapons)):
					self.damage = self.weapons[weapon_num].damage
					self.weapons[weapon_num].count -= 1
					if self.weapons[weapon_num].count <= 0:
						self.weapons.pop(weapon_num)
					break
				print("Введите номер существующего оружия: ")
			except ValueError:
				print("Введи число: ")

class Game:

	def load_config(self):
		with open("config.json","rt",encoding="utf-8") as f:
			return f.read()


	def load_weapons(self,config):
			weapons = json.loads(config)["weapons"]
			# print(weapons)
			return [Weapon(name,ch["damage"],0,ch["count"]) for name, ch in weapons.items()]

	def give_weapon(self,player,weapons):
		if not random.randint(0,3):
			this_weapon = random.choice(weapons)
			this_weapon.count += this_weapon.original_count
			if this_weapon not in player.weapons:
				player.weapons.append(this_weapon)
			print(this_weapon.name,"полученно")


	def start(self):
		config = self.load_config()
		weapons = self.load_weapons(config)
		# print(weapons)
		player = Player("Залик", 1000, 50, [Weapon("Отвертка", 10, 999, 999)])
		livingdead = Zombie("Зомби-обычный", 300, 20)
		count = 0
		while True:
			self.give_weapon(player,weapons)

			player.show_weapons()
			player.choose_weapon()
			player.attack(livingdead)
			livingdead.attack(player)
			player.show_stats()
			livingdead.show_stats()
			input("-"*10)
			if player.hp <= 0:
				print("Вы умерли и заработали {0} очков".format(count))
				break
			if livingdead.hp <= 0:
				print("Появляется новый зомби")
				livingdead = Zombie("Зомби-обычный", 60, 20)
				count += 1

game = Game()
game.start()