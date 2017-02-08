class Human:
	def __init__(self, name, iq, weight, age):
		self.name = name
		self.iq = iq
		self.weight = weight
		self.age = age

	def move(self):
		print(self.name, "сдвинулся")

gadzhimagomed = Human("Гаджимагомед", 184, 50, 16)
print(gadzhimagomed.name)
print(gadzhimagomed.iq)
gadzhimagomed.weight += 5 
print(gadzhimagomed.weight)
amin = Human("'Абдул'Амин",121,70,12)
amin.move()