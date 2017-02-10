class Skeleton:
	pass

class Necro:
	def __init__(self):
		self.mp = 100

	def summon(self):
		self.mp -= 10
		return Skeleton


zalik = Necro()
skelet1 = zalik.summon()

print(zalik.mp)