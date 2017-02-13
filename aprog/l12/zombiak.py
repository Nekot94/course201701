class Weapon:
	def __init__(self,name,damage,count):
		self.name = name
		self.damage = damage
		self.count = count

class Character :
	def __init__(self,name,hp,damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	
	def attack(self,victim):
		victim.hp -= self.damage
		print("{0.name} нанёс {1.name} {0.damage} урона".format(self,victim))

class Zombie(Character):
	pass

class Player(Character):

	def __init__(self,name,hp,damage,weapon):
		super().__init__(name,hp,damage)
		self.weapon = weapon
	def attack(self,victim):
		dmg = self.damage + self.weapon.damage
		victim.hp -= dmg
		self.weapon.count -= 1
		print("{0.name} нанёс {1.name} {2} урона".format(self,victim,dmg))


class Game:
	def start():
		weapon = Weapon("SUperPuper",189, 5)
		player = Player("Кадырл",1000,100,weapon)
		zombie = Zombie("Аркадий паравозов", 500, 50)
		count = 0
		while True:
			player.attack(zombie)
			zombie.attack(player)
			input()
			if player.hp <= 0 :
				print("Ты умер !!! и получил {0} очков".format(count))
				break
			if zombie.hp <= 0 :
				zombie = Zombie("Аркадий паравозов", 500, 50)
				count += 1
				print("Ты убил зомби")


Game.start()