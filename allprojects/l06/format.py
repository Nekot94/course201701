# форматирование
name = "Абдурахаман"
age = 11
foolness = 4.5
print("Твое имя "+name+", твой возраст "+str(age)+", твоя глупость "+str(foolness))

print("Твое имя %15.8s, твой возраст %10.10d, твоя глупость %10.1f%%" %(name, age, foolness))
name = "Иса"
print("Твое имя %15s, твой возраст %10d, твоя глупость %10f%%" %(name, age, foolness))

print("Твое имя {2}, твой возраст {0}, твоя глупость {1}%".format(name, age, foolness))
print("Твое имя {0}, твой возраст {0}, твоя глупость {0}%".format(name, age, foolness))
print("Твое имя {0:3^10s}, твой возраст {1}, твоя глупость {2}%".format(name, age, foolness))

glupci = {"Арсен":9999,"Ахмед":666,"Гомер":9000}

print("Арсен: {0[Арсен]}, Ахмед: {0[Ахмед]}".format(glupci))