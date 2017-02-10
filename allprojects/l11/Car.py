class Car:
	def __init__(self,speed,color,protection):
		self.speed = speed
		self.color = color
		self.protection = protection
		self.super_power = False
		print(self)
	
	def crash(self):
		self.protection -= self.speed
		print ("Бабах!!!")
		if self.protection <= 0:
			print("Мёртв")
