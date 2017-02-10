class Mage:
	def __init__(self, name, hp, mp, skill_power):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.skill_power = skill_power

	def move(self):
		print(self.name,"пошел куда-то")

	def cast(self, cost, target):
		self.mp -= cost
		damage = self.skill_power * cost // 100
		target.hp -= damage
		print(target.name,"бахнуло магией на", damage ," урона")
		

class WaterMage(Mage):
	def __init__(self, name, hp, mp, skill_power, water_resist):
		super().__init__(name, hp, mp, skill_power)
		self.water_resist = water_resist

	def cast(self, cost, target, life_drain):
		super().cast(cost, target)
		self.hp += life_drain 
		self.mp -= life_drain * 2

	def ice_arrow(self, target):
		self.mp -= 50
		target.hp -= self.skill_power // 2
		print(target.name,"бахнуло льдом на",self.skill_power," урона")

class FireMage(Mage):
	def fire_ball(self, target):
		self.mp -= 100
		target.hp -= self.skill_power
		print(target.name,"бахнуло огнем на",self.skill_power," урона")

saturas = WaterMage("Сатурас",640,1000,175, water_resist = 0)
vatras = WaterMage("Ватрас",280,1000,100, 78)
saturas.ice_arrow(vatras)
vatras.cast(1000,saturas, 100)

milton = FireMage("Милтон",150,1000,500)
milton.fire_ball(saturas)
milton.cast(100, saturas)







