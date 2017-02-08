class Priest:
	def __init__(self,name,hp,heal_power,mana):
		self.name = name
		self.hp = hp
		self.heal_power = heal_power
		self.mana = mana

	def move(self):
		print(self.name,"пошел далеко")

	def heal(self, target):
		try:
			target.hp += self.heal_power
			self.mana -= 100
			print("{0.name} вылечили на {1.heal_power}".format(target,self))
		except AttributeError:
			print("Ты бы еще стул вылечил")





gadjheel = Priest("Ардуин05",400,20,900)

print(gadjheel.name)
print(gadjheel.heal_power)
gadjheel.heal_power += 10
print(gadjheel.heal_power)

gadjheel.move()
gadjheel.move()
gadjheel.move()

gadjheel.heal(gadjheel)
print(gadjheel.hp)
print(gadjheel.mana)

tigr05 = Priest("Жрец-Тигр-Красавчик-05-Пантера",20,10,1000000)

gadjheel.heal(tigr05)
print(tigr05.hp)
print(gadjheel.mana)