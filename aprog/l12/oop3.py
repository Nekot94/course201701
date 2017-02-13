class Shaurma:
	count = 0

	# def get_count():
	# 	print("Количество шаурмы:", Shaurma.count)

	@classmethod
	def get_count(cls):
		print("Количество шаурмы:", cls.count)

	def __init__(self, kind, cost, size):
		self.kind = kind
		self.cost = cost
		self.__size = size
		Shaurma.count += 1
	
	def __del__(self):
		Shaurma.count -= 1
		print("Шаурма умерла")

	def poison(self, eater):
		if self.__size > 0:
			print("{0}, был отравлен шаурмой {1.kind}".format(
				eater, self))
			self.__size -= 5
		else:
			print("Шаурмы больше нет")


	# def get_size(self):
	# 	return self.__size

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, value):
		print("Шаурма возродилась")
		self.__size = value

	def __add__(self, other):
		return Shaurma("Мегашаурам!!!", 
			(self.cost + other.cost) * 10,
			self.size + other.size)

	def __str__(self):
		return "Шаурма: {0.kind}, цена: {0.cost}, длина: {0.size}см".format(self)


Shaurma.get_count()
chicken_shaurma	= Shaurma("куриная", 70, 15)
print(chicken_shaurma)
chicken_shaurma.poison("Джавид")

meat_shaurma = Shaurma("мясная в булочке", 70, 15)
print(meat_shaurma)
meat_shaurma.poison("Амин")
print()
meat_shaurma.poison("Кадыр")
meat_shaurma.poison("Гуд")
# meat_shaurma.__size += 100
# print(meat_shaurma.get_size())
# del chicken_shaurma
meat_shaurma.size += 15
print(meat_shaurma.size)
meat_shaurma.poison("Камал")
Shaurma.get_count()
mega_shauren = chicken_shaurma + meat_shaurma
print(mega_shauren)
