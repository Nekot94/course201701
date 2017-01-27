a = "Амин красавчик"
b = 6
c = 6.1
e = True
n = None
print(a, b, c, e, n)
print(type(a), type(b), type(c))
print(type(e), type(n))
# print(a[0] + a[1] + a[2] + a[3])
print(a[0:4])
print(a[5:])
print(a[-3:])
print(a[-1:-4:-1])
print(len(a))
poem = """  Закали свои порывы,
  Преврати порывы в сталь,
  И лети мечтой игривой,
  Ты в заоблачную даль!"""
print(poem)
print(poem.find("порывы"))
print(poem.rfind("порывы"))
print(poem.count("порывы"))

print(poem.upper())
print(poem.lower())
print(poem.title())

print(poem.replace("порывы","эликсиры"))

print(a[0])

krasavci = ["Кадыр","Амин","Аслан"]
print(krasavci[1:])
krasavci.append("Мага")
print(krasavci)
krasavci.insert(1,"Мага")
print(krasavci)
dop = ["Арслан","Амин"]
krasavci.extend(dop)
print(krasavci)
krasavci[2] = 3
print(krasavci)
del krasavci[0]
print(krasavci)
krasavci.remove("Арслан")
print(krasavci)
print(krasavci.pop(1))
print(krasavci)

str1 = " <3 ".join(krasavci)
print(str1)
print(str1.split('<3 '))

krasavci2 = "Камал", "Гуд"
print(krasavci2)
krasavci2 = list(krasavci2)
krasavci2[1] = "<3"
print(krasavci2)

krasavci3 = {1, 2, 3, 1, 5}
krasavci4 = {1, 9, 3, 4}

print(krasavci3)
print(krasavci4)
# print(1 in krasavci3)
# krasavci3.add(8)
# print(krasavci3)

print(krasavci3 & krasavci4) # пересечение
print(krasavci3 | krasavci4) # обьединение
print(krasavci4 - krasavci3) # разность