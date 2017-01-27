word = "Ты, я - красавчики"
# number = 98
# number2 = 3.42
# boolean = False
# the_best = None
# print(word,number,number2,boolean,the_best)
# print(type(word),type(number))
# print(type(boolean),type(the_best))
# print(word[::-1])
# print(len(word))
# stih = '''  Пейте смело, друзья! В час веселых утех
#   Усладят нас свирель, гимны зелью и смех.
#   Что ж до судного дня - он, похоже, не завтра,
#   Может быть, позабудут наш маленький грех.'''
# print(stih)
# print(stih.find(", "))
# print(stih.rfind(", "))
# print(stih.count(","))

# print(stih.upper())
# print(stih.lower())
# print(stih.title())

# print(stih.replace("дня","пня"))
# print(stih)

loxy = ["Иса", "Расул", "Магомедрасул"]
print(loxy[0:2])
loxy.append("Магомед")
print(loxy)
list2 = ["Русик","Артур"]
loxy.extend(list2)
print(loxy)
loxy.insert(2,"Магомед")
print(loxy)
loxy[0] = 3
print(loxy)
del loxy[0]
print(loxy)
loxy.remove('Русик')
print(loxy)
print(loxy.pop(-1))
print(loxy)
loxy.append("гамид")
loxy.sort()
print(loxy)
loxy.sort(reverse=True)
print(loxy)
ne_loxi = "Саид", "Гаджимурад"
print(ne_loxi)
# ne_loxi[0] = "Cиид"
super_loxi = {8, 1, 4, 1, 5}
super_loxi2 = {9, 4, 5}
print(super_loxi)
# super_loxi.add(6)
print(super_loxi)
print(9 in super_loxi)
print(super_loxi & super_loxi2)
print(super_loxi | super_loxi2)
print(super_loxi - super_loxi2)
print(set(loxy))


