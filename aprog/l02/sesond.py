

print("Амин тигр")
print(5 + 5)
minsus = "5"
Артур = 3
print(minsus, Артур)
Артур = Артур + 2
print(Артур)
Артур *= 4 # Артур = Артур * 4
print(Артур)
a = input("Введите имя  ")
print("Твое имя -", a)
b = input("Введите число: ")
b = int(b)
print("Твое число + 5", b + 5)

import math


# # a = int(input("Введите значение гипотенузы: "))
# b = int(input("Введите значение первого катета "))
# с = int(input(math.sqrt((a*a)-(b*b))))
# print(c)

# a = int(input("Введите число"))
# b = int(input("Введите число"))
# с = a + b
# a = c - a
# b = c - b
# print(a)
# print(b)

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите с: "))
d = b * b - 4 * a * c
x1 = (-b - math.sqrt(d))/ (2 * a)
x2 = (-b + math.sqrt(d))/ (2 * a)
print("Введите корень:",x1)
print("Введите корень:",x2)