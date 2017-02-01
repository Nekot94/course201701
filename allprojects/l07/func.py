def hello(name):
	print("Привет, {0}!!!".format(name))


hello("Гамида")
hello("Залим")
name = "Арсен"
hello(name)


def sum5(a, b):
	s = a + b + 5
	return s

print(sum5(2,5))
ss = sum5(4,5)
print(ss + 1)

# def input_number():
# 	while True:
# 		try:
# 			number = int(input("Введите число"))
# 			return number
# 			break
# 		except ValueError:
# 			print("Это не число!")

# n1 = input_number()
# n2 = input_number()
# print("{0} это сумма введенных чисел".format(n1 + n2))
print(hello("ТТТ"))


def get_two_value_from_list(my_list):
	return my_list[0], my_list[1]

a, b  = get_two_value_from_list([5,"саид",8,1])

print(a, b)

a, b, c = 5, 6, (7, 8)

print(a, b, c)

d, e = c

print(d, e)

print(sum5(b=2,a=4))

def hello2(name,target="лес"):
	print("{0}, пошел в {1}".format(name,target))

hello2("Гамид")
hello2("Арсын","помойку")
hello2("Арсын",target = "помойку")

print(1,end=" ")
print(2)

def show_articles(*args):
	for article in args:
		print("Товар:", article, end=" ")
	print()

show_articles(7, "машинка", "динамит", "пара кукол")


def show_info(**kwargs):
	for key, value in kwargs.items():
		print("{0}: {1}".format(key,value))

show_info(name="the Best",age="durachok")

num = 5

def mul5(a, b):
	global num
	num = 6
	return num

print(mul5(3,3))
print(num)

list1 = ["лох1", "лох2"]

def add_loh(my_list, number):
	my_list.append("лох" + str(number))

add_loh(list1,3)
print(list1)
list2 = list1
add_loh(list1,4)
print(list2)



	