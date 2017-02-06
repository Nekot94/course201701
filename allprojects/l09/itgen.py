# lst1 = ["Made", "in", "China"]
# lst1 = iter(lst1)
# print(lst1)
# print(next(lst1))
# print(next(lst1))
# print(next(lst1))
# print(next(lst1))

# lst2 = [4, 5, 6]
# for i in lst2:
# 	print(i)

# lst2 = iter([4, 5, 6])
# while True:
# 	try:
# 		print(next(lst2))
# 	except StopIteration:
# 		break

# for i in 'абвгде':
# 	print(i)

# lst2 = [1, -1, 4, 5]
# print(len(lst2),sum(lst2),min(lst2),max(lst2))
# print(all(lst2),any([[],{},"",0,None]))

# lst3 = [5, 8, 100]


# for i, j, k in zip(lst2, lst3, [9, 2]):
# 	print(i, j, k)

# names = 'Иса', 'МагомедРасул'
# for num, names in enumerate(names,100):
# 	print(num,names)


# g1 = []
# for i in range(1,51):
# 	if i % 2 == 0:
# 		g1.append(i)

# print(g1)

# g2 = [i for i in range(1,51) if not i % 2]
# print(g2)

# names = ['Магомед','Ахмед']
# nicknames = ['Сенсей','Чебурек','Валера']
# res = []
# for i in names:
# 	for j in nicknames:
# 		res.append((i,j))

# print(res)

# res = [(i, j) for i in names for j in nicknames if (i, j) != ('Магомед','Валера')]
# print(res)

from random import randint

def random_range(start,stop,step=1):
	i = start
	while i < stop:
		yield randint(start,stop-1)
		i += step;

for i in random_range(1,10):
	print(i)
