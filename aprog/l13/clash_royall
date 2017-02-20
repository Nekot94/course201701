import random 

gold = 100
gem = 10

class Unit:
    def __init__(self, name, number, gold, call):
        self.name = name
        self.number = number
        self.gold = gold
        self.call = call
srely = Unit("Стрелы", 1, 10, 0)
knight = Unit("Рыцарь", 2, 10, 0)
archers = Unit("Лучницы", 3, 10, 0)
demoman = Unit("Бомбер", 4, 10, 0)
giant = Unit("Гигант", 5, 30, 0)
pitch_min = Unit("Мини пека", 6, 30, 0)
fire_ball = Unit("Огненый шар", 7, 30, 0)
musketeer = Unit("Мушкетёр", 8, 30, 0)
super_puper = Unit("Супер-пупер-карта", 228, 500, 0)

while gold >= 0:
    print()
    print(gold,"золота", gem,"кристалов")
    a1 = int(input("""
1--------ОТКРЫТЬ СУНДУК--------
2---------ПРОСМОТР-КАРТ--------
3---------ПРОДАЖА-КАРТ---------
4------------В-БОЙ-------------
5----Я-ПЕРВЫЙ-РАЗ-ОТКРЫЛ-ИГРУ--
6-----------МАГАЗИН------------
-----------------------------------------------------------------------------------------------------------------------"""))
    if a1 == 1:
        print()
        print(gold,"золота", gem,"кристалов")
        c1 = int(input("""
1-------ОБЫЧНЫЙ-СУНДУК---------30 золота
2-------ЗОЛОТОЙ-СУНДУК---------100 золота
3------ЭПИЧЕСКИЙ-СУНДУК--------300 золота
----------------------------------------------------------------------------------------------------------------------"""))
        if c1 == 1:
            if gold < 30:
                print()
                print("У ТЕБЯ НЕТ ЗОЛОТА ПРОДАЙ КАРТЫ")
            else:
                gold -= 30
                x = random.randint(1,4)
                if x == srely.number:
                    srely.call += 1
                    print()
                    g = random.randint(10,30)
                    print(g,"золота")
                    gold += g
                    print()
                    print(srely.name, 1)
                elif x == knight.number:
                    knight.call += 1
                    print()
                    g = random.randint(10,30)
                    print(g,"золота")
                    gold += g
                    print()
                    print(knight.name, 1)
                elif x == demoman.number:
                    demoman.call += 1
                    print()
                    g = random.randint(10,30)
                    print(g,"золота")
                    gold += g
                    print()
                    print(demoman.name, 1)
                elif x == archers.number:
                    archers.call += 1
                    print()
                    g = random.randint(10,30)
                    print(g,"золота")
                    gold += g
                    print()
                    print(archers.name, 1)

        elif c1 == 2:
            if gold < 100:
                print()
                print("У ТЕБЯ НЕТ ЗОЛОТА ПРОДАЙ КАРТЫ")
            else:
                gold -= 100
                x1 = random.randint(1,3)
                if x1 == srely.number:
                    x4 = random.randint(1,3)
                    srely.call += x4
                    print()
                    g2 = random.randint(30,70)
                    print(g2,"золота")
                    gold += g2
                    print()
                    print(srely.name, x4)
                elif x1 == knight.number:
                    x4 == random.randint(1,3)
                    knight.call += x4
                    print()
                    g2 = random.randint(30,70)
                    print(g2,"золота")
                    gold += g2
                    print()
                    print(knight.name, x4)
                elif x1 == demoman.number:
                    x4 = random.randint(1,3)
                    demoman.call += x4
                    print()
                    g2 = random.randint(30,70)
                    print(g2,"золота")
                    gold += g2
                    print()
                    print(demoman.name, x4)
                elif x1 == archers.number:
                    x4 = random.randint(1,3)
                    archers.call += x4
                    print()
                    g2 = random.randint(30,70)
                    print(g2,"золота")
                    gold += g2
                    print()
                    print(archers.name, x4)
                x2 = random.randint(5,8)
                if x2 == giant.number:
                    giant.call += 1
                    print()
                    g3 = random.randint(1,2)
                    print(g3,"кристалов")
                    gem += g3
                    print()
                    print(giant.name, 1)
                elif x2 == pitch_min.number:
                    pitch_min.call += 1
                    print()
                    g3 = random.randint(1,2)
                    print(g3,"кристалов")
                    gem += g3
                    print()
                    print(pitch_min.name, 1)
                elif x2 == musketeer.number:
                    musketeer.call += 1
                    print()
                    g3 = random.randint(1,2)
                    print(g3,"кристалов")
                    gem += g3
                    print()
                    print(musketeer.name, 1)
                elif x2 == fire_ball.number:
                    fire_ball.call += 1
                    print()
                    g3 = random.randint(1,2)
                    print(g3,"кристалов")
                    gem += g3
                    print()
                    print(fire_ball.name, 1)

        elif c1 == 3:
            if gold < 300:
                print()
                print("У ТЕБЯ НЕТ ЗОЛОТА ПРОДАЙ КАРТЫ")
            else:
                x5 = random.randint(1,4)
                print("ВВЕДИТЕ ЧИСЛО ЛЮБОЕ")
                a2 = int(input(""))
                if a2 == x5:
                    print("ТЫ ВЫЙГРАЛ СУПЕР ПУПЕР КАРТУ")
                    super_puper.call += 1
                    if gold >= 40:
                        gold += random.randint(-40,40)
                    else:
                        gold -= gold
                else:
                    print("ТЫ ПРОИГРАЛ")


    elif a1 == 2:
        print()
        print(gold,"золота", gem,"кристалов")
        print()
        print(srely.name, srely.call)
        print(knight.name, knight.call)
        print(archers.name, archers.call)
        print(demoman.name, demoman.call)
        print(giant.name, giant.call)
        print(pitch_min.name, pitch_min.call)
        print(musketeer.name, musketeer.call)
        print(fire_ball.name, fire_ball.call)

    elif a1 == 3:
        print()
        print(gold,"золота", gem,"кристалов")
        print()
        print("Скопируйте имя персонажа которого желаете продать ")
        p1 = input("")
        print("Выберите сколько карт вы хотите продать")
        p2 = int(input(""))
        if p2 < 1:
            print("ТЫ ДУМАЕШЬ ЧТО ТЫ САМЫ УМНЫЙ?????")
        else:    
            if p1 == srely.name and p2 <= srely.call:
                if srely.call > 0:
                    srely.call -= p2
                    gold += srely.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",srely.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

            elif p1 == knight.name and p2 <= knight.call:
                if knight.call > 0:
                    knight.call -= p2
                    gold += knight.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",knight.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

            elif p1 == archers.name and p2 <= archers.call:
                if archers.call > 0:
                    archers.call -= p2
                    gold += archers.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",archers.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

            elif p1 == demoman.name and p2 <= demoman.call:
                if demoman.call > 0:
                    demoman.call -= p2
                    gold += demoman.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",demoman.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

            elif p1 == fire_ball.name and p2 <= demoman.call:
                if fire_ball.call > 0:
                    fire_ball.call -= p2
                    gold += fire_ball.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",fire_ball.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

            elif p1 == giant.name and p2 <= giant.call:
                if giant.call > 0:
                    giant.call -= p2
                    gold += giant.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",giant.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

            elif p1 == musketeer.name and p2 <= musketeer.call:
                if musketeer.call > 0:
                    musketeer.call -= p2
                    gold += musketeer.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",musketeer.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

            elif p1 == pitch_min.name and p2 <= pitch_min.call:
                if pitch_min.call > 0:
                    pitch_min.call -= p2
                    gold += pitch_min.gold * p2
                    print("ВЫ ПРОДАЛИ КАРТУ",pitch_min.name)
                    print()
                    print(gold,"золота", gem,"кристалов")
                else:
                    print("У ВАС НЕТ ДАНОЙ КАРТЫ В НАЛИЧИИ")

    elif a1 == 4:
        print("Выберите карту за которую будете играть")
        v1 = input("")
        if v1 == srely.name:
            print("Выберите количество",srely.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= srely.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    srely.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    srely.call -= v2 
            else:
                print("Возникли проблемы с даными")  

        elif v1 == knight.name:
            print("Выберите количество",knight.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= knight.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    knight.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    knight.call -= v2 
            else:
                print("Возникли проблемы с даными")

        elif v1 == archers.name:
            print("Выберите количество",archers.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= archers.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    archers.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    archers.call -= v2 
            else:
                print("Возникли проблемы с даными")

        elif v1 == demoman.name:
            print("Выберите количество",demoman.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= demoman.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    demoman.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    demoman.call -= v2 
            else:
                print("Возникли проблемы с даными")

        elif v1 == giant.name:
            print("Выберите количество",giant.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= giant.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    giant.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    giant.call -= v2 
            else:
                print("Возникли проблемы с даными")

        elif v1 == pitch_min.name:
            print("Выберите количество",pitch_min.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= pitch_min.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    pitch_min.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    pitch_min.call -= v2 
            else:
                print("Возникли проблемы с даными")

        elif v1 == musketeer.name:
            print("Выберите количество",musketeer.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= musketeer.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    musketeer.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    musketeer.call -= v2 
            else:
                print("Возникли проблемы с даными")

        elif v1 == fire_ball.name:
            print("Выберите количество",fire_ball.name)
            v2 = int(input(""))
            if v2 > 0 and v2 <= fire_ball.call:
                bot = random.randint(1,3)
                if 1 == bot:
                    print("ТЫ ВЫЙГРАЛ",v2,"КАРТ")
                    fire_ball.call += v2
                elif 1 != bot:
                    print("ТЫ ПРОИГРА",v2,"КАРТ")  
                    fire_ball.call -= v2 
            else:
                print("Возникли проблемы с даными")

    elif a1 == 6:
        print()
        print("""
Выберите команду:
1--------ОБМЕН-КРИСТАЛОВ----------------
2-------СУПЕР-ПУПЕР-СУНДУК--------------
3--------------ДАНАТ--------------------""")
        c2 = int(input(""))
        if c2 == 1:
            c3 = int(input("Сколько кристалов вы хотите обменять 1 кристал - 30 золота "))
            if c3 > 0 and c3 <= gem:
                gold += c3 * 30
                gem -= c3
                print()
                print("Вам зачисле",c3 * 30,"золота")
                print()
                print(gold,"золота", gem,"кристалов")
            else:
                print("Возникли проблемы с даными")

        elif c2 == 2:
            print("---------------------------СУПЕР-ПУПЕР-СУНДУК-------------------------------100-ГЕМОВ")
        else:
            print("Возникли проблемы с даными")




    else:
        print("""
НАЧНЁМ ПО ПОРЯДКУ
В ПЕРВОМ ПОЛЕ ТЫ МОЖЕШЬ ОТКРЫТЬ ОДИН ИЗ ТРЁХ СУНДУКОВ
КАЖДЫЙ СТОИТ ПО РАЗНОМУ ПОКУПАЮТСЯ СУНДУКИ ЗА ЗОЛОТО ИЛИ КРИСТАЛЫ
ИЗ НИХ ВЫПАДАЮТ КАРТЫ КОТОРЫЕ ТЫ МОЖЕШЬ ПРОДАТЬ ИЛИ ПРОСМОТРЕТЬ
КАРТЫ НУЖНЫ ДЛЯ БОЯ У КАЖДОЙ КАРТЫ СВОЙ ВИД БОЯ
ЗА ПОБЕДУ ТЫ ПОЛУЧАЕШЬ КАРТЫ ИЛИ ТЕРЯЕШЬ В ЗАВИСИМОСТИ ОТ
ТОГО ВЫЙГРАЕШЬ ТЫ ИЛИ ПРОИГРАЕШЬ 
В МАГАЗИНЕ ТЫ МОЖЕШЬ ОБМЕНЯТЬ КРИСТАЛЫ НА ЗОЛОТО
КУПИТЬ СУПЕР-ПУПЕР СУНДУКИ И ЗАДОНАТИТЬ""")