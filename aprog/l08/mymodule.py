__version__ = '0.1'
kingdoms = {
	'Растения':{'Роза','Ромашка'},
	'Животные':{'Волк','Лиса','Кадыр'}
}

def find_kingdom(thing):
	for kingdom in kingdoms:
		if thing in kingdoms[kingdom]:
			return kingdom

	else:
		return "Нет такого царства"


if __name__ == "__main__":
	print(find_kingdom('Роза'))

