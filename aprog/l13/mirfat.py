import random

gold = 100

class Unit:
    def __init__(self, name, cena, calic):
        self.name = name
        self.cena = cena       
        self.calic = calic     

strelu = Unit("Стрелы", 10, 0)
bomber = Unit("Бомбер", 10, 0)
luchicu = Unit("Лучницы", 10, 0)
rucar = Unit("Рыцарь", 10, 0)    
peca = Unit("Мини пека", 30, 0)
muhcet = Unit("Мушкетёр", 30, 0)
ognenuhar = Unit("Огненый шар", 30, 0)
gigant = Unit("Гигант", 30, 0)
vedma = Unit("Ведьма", 50, 0)
princ = Unit("Принц", 50, 0)
dracon = Unit("Дракон", 50, 0)
scelet = Unit("Орда скелетов", 50, 0)


class Chest:
    def __init__(self, cena, name, gold, cartu):
        self.cena = cena
        self.name = name
        self.gold = gold
        self.cartu = cartu

free_chest = Chest(30, "Бесплатный сундук", random.randint(20, 50), random.randint(1, 4))
if free_chest.cartu == 1:
    free_chest.cartu = strelu.name
    strelu.calic += 1
elif free_chest.cartu == 2:
    free_chest.cartu = bomber.name
    bomber.calic += 1
elif free_chest.cartu == 3:
    free_chest.cartu = luchicu.name
    luchicu.calic += 1     
elif free_chest.cartu == 4:
    free_chest.cartu = rucar.name
    rucar.calic += 1

gold_chest = Chest(50, "", random.randint(30, 70), random.randint(1,4))  
if gold_chest.cartu == 1:
    gold_chest.cartu = muhcet.name
    muhcet.calic += 1
elif gold_chest.cartu == 2:
    gold_chest.cartu = peca.name 
    muhcet.calic += 1
elif gold_chest.cartu == 3:
    gold_chest.cartu = ognenuhar.name
    ognenuhar.calic += 1
elif gold_chest.cartu == 4:
    gold_chest.cartu = gigant.name 
    gigant.calic += 1

while gold > 0:
    print("""Что будем делать
1)Открыть сундук
2)Посмотреть карты
3)Продать карты        """)
    a1 = int(input(""))
    if a1 == 1:
        a = int(input("Выберите сундук 1)Бесплатный сундук 2)Золотой сундук 3)Эпический сундук"))
        if a == 1:
            gold -= free_chest.cena
            print("Цена", free_chest.cena, "золота")
            print("Название", free_chest.name) 
            print(free_chest.gold ,"золота") 
            print(free_chest.cartu)
            gold += free_chest.gold
            print("У вас", gold ,"золота")
        elif a == 2:
            gold -= gold_chest.cena
            print("Цена", gold_chest.cena, "золота")
            print("Название", gold_chest.name) 
            print(gold_chest.gold ,"золота") 
            print(gold_chest.cartu)
            gold += gold_chest.gold
            print("У вас", gold ,"золота") 

    elif a1 == 2:
        print(strelu.name)
        print(strelu.cena)
        print(strelu.calic)
        print(bomber.name)
        print(bomber.cena)
        print(bomber.calic)
        print(luchicu.name)
        print(luchicu.cena)
        print(luchicu.calic)
        print(rucar.name)
        print(rucar.cena)
        print(rucar.calic)
        print(muhcet.name)
        print(muhcet.cena)
        print(muhcet.calic)
        print(peca.name)
        print(peca.cena)
        print(peca.calic)
        print(ognenuhar.name)
        print(ognenuhar.cena)
        print(ognenuhar.calic)
        print(gigant.name)
        print(gigant.cena)
        print(gigant.calic)
        print(princ.name)
        print(princ.cena)
        print(princ.calic)
        print(vedma.name)
        print(vedma.cena)
        print(vedma.calic)
        print(scelet.name)
        print(scelet.cena)
        print(scelet.calic)
        print(dracon.name)
        print(dracon.cena)
        print(dracon.calic)
    elif a1 == 3:
        print("")