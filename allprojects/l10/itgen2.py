list1 = [i for i in "абвгде" if i != "г"]
print(list1)
import random
# from copy import copy

def generat(elem):
	# r = copy(elem)
	try:
		r = list(elem)[:]
		while r:
			temp = random.choice(r)
			yield temp
			r.remove(temp)
	except TypeError:
		print("Введите что-то что можно превратить в список")

mmm = 678
for i in generat(mmm):
	print(i)
print(mmm)
