# list1 = ["А","Арбуз","Амин"]
# list1 = iter(list1)
# print(list1)
# print(next(list1))
# print(next(list1))
# print(next(list1))
# print(next(list1))

# list1 = [4, 5, 6]
# for i in list1:
# 	print(i)

# list1 = [4, 5, 6]
# list2 = iter(list1)
# while True:
# 	try:
# 		print(next(list2))
# 	except StopIteration:
# 		break 

# for i in "Абураха":
# 	print(i)

# list2 = [4, 5, -1, 0]
# print(len(list2),sum(list2),max(list2),min(list2))
# print(any(['',0,None,{},(),[],False]),all(list2))

# list1 = [6, 7, 8, 9]
# list2 = [5,'Кадыр',78]
# for n1, n2, n3 in zip(list1, list2, [4,5]):
# 	print(n1, n2, n3)

# names = ['Джавид',"Green Giant"]
# for num, name in enumerate(names):
# 	print(num, name)

# l1 = []
# for i in range(1,51):
# 	if i != 10:
# 		l1.append(i)
# print(l1)

# l2 = [k for k in range(1,51) if k != 10]
# print(l2)

# names = ["Казбек","Джамиля"]
# nicknames = ["Гундерсон","Белый","Алкаш"]
# result = []
# for name in names:
# 	for nickname in nicknames:
# 		result.append((name, nickname))
# print(result)
# result = [(n, ni) for n in names for ni in nicknames ]
# print(result)

import random

def random_rage(start, stop, step = 1):
	i = start
	alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	while i < stop:
		yield random.choice(list(alphabet))
		i += step

print(random_rage(1,50))
for i in random_rage(1,10):
	print(i)





