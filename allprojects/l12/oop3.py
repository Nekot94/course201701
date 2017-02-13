class Undead:
	count = 0

	# @classmethod
	# def show_zombie(cls):
	# 	print("Колличество зомби", cls.count)

	def show_zombie():
		print("Колличество зомби", Undead.count)

	def __init__(self,name,hp,power):
		self.name = name
		self.hp = hp
		self.power = power
		self.__hands = 2
		Undead.count += 1

	@property
	def hands(self):
		# print("выводим руки")
		return self.__hands

	@hands.setter
	def hands(self, count):
		if count > 2:
			count = 2
		if count < 0:
			print("с ума сошел что ли")
			count = self.__hands
		self.__hands = count
		
	def attack(self,target):
		if self.__hands:
			target.hp -= self.power
			print("{0.name} ударил {1.name} и нанес {0.power}".format(
				self,target))
			self.__hands -= 1
			if target.hp <= 0:
				print(target.name,"умер")
		else:
			print("Бить без рук {0.name} не может".format(self))

	def __add__(self,other):
		return Undead("Мясник",self.hp + other.hp, 
			self.power + other.power )


	def __str__(self):
		return "{0.name}, жизни: {0.hp} сила:{0.power}".format(self)

	def __del__(self):
		Undead.count -= 1


Undead.show_zombie()
clara = Undead("Клара",500,150)
david = Undead("Давид",300,50)

print(clara.hands)
clara.attack(david)
clara.attack(david)
clara.attack(david)
clara.attack(david)
clara.hands = 10
clara.attack(david)
clara.attack(david)
clara.hands = -5
clara.attack(david)
clara.attack(david)
clara.attack(david)

print(clara)


david2 = Undead("Давид",300,50)
Undead.show_zombie()

butcher = david2 + clara
print(butcher)


