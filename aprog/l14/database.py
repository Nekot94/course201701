# f = open("data.txt","wt")
# a = """Вася|Петров|Ивановия|FunnyROid|100000,Евгений|Мартиров|iOSович|ROckrek|100000"""
# f.write(a)
# f.close()
def getData(filename):
	text = open(filename,"rt",encoding="utf-8").read()
	peoples = text.split(",")
	peoples2 = list()
	for people in peoples:
		p = people.split("|")
		peoples2.append(p)
	datas = list()
	for man in peoples2:
		newchel = dict()
		newchel["Name"] = man[0]
		newchel["Surname"] = man[1]
		newchel["Otchestvo"] = man[2]
		newchel["Company"] = man[3]
		newchel["Cash"] = int(man[4])
		datas.append(newchel)
	return datas
def printData(dt):
	for this in dt:
		print("Владелец : {3} - {0}  {1}  {2} имеет {4} денег".format(this["Name"],this["Surname"],this["Otchestvo"],this["Company"],this["Cash"]))
f = open("data.txt","at", encoding="utf-8")

data = getData("data.txt")


select = input("1 - прочитать, 2 - записать")
if select == "1" :
	printData(data)
if select == "2":
	x = ","+input("Имя владельца")+"|"+input("Фамилия владельца")+"|"+input("Отчество владельца")+"|"+input("Название компании")+"|"+input("Количество денег")
	f.write(x)