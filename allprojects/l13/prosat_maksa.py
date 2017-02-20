import random

class Character:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	def attackbaz(self, target):
		crita = random.randint(0,8)
		if crita == 1:
			target.hp -= self.damage
			target.hp -= self.damage
			print("{0.name} нанёс {1.name} КРИТИЧЕСКИЙ урон! Твоё здоровье: {0.hp}".format(self, target, self))
			input()
		if crita != 1:
			target.hp -= self.damage
			print("{0.name} нанёс {1.name} {0.damage} урона! Твоё здоровье: {0.hp}".format(self, target, self, self))
			input()
playerInventory = {"Острая сабля":"Острее твоих шуток"}

class KonetzError:
	pass
class Toiletambal():
	def __init__(self, name,hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	def ambalattack(self, target):
		target.hp -= self.damage
		print("{0.name} ударил {1.name}, нанеся {0.damage} урона! Здоровье амбала {0.hp}".format(self, target, self, target))
class Toltol(Toiletambal):
	pass
class Tolotos(Toiletambal):
	def heal(self):
		if self.hp <= 80: 
			self.hp += 20


def PrintCharar():
	print( " Удар саблей - {0.damage}")

def OpenInventory():
    while True:
        try:
            print(list(playerInventory.keys()))
            infunc = input("Это ваши предметы. Введи название предмета, чтобы посмотреть его описание. Для выхода нажмите 1")
            if infunc == "1":
                break
            if infunc != 1:
                print(playerInventory[infunc])
                input()
        except KeyError:
            print("Неверно введено название предмета")
            input()

def Chelovek():
	print("Монстр: Минутку, так ты.. ЧЕЛОВЕК?")
	input()
	print("Кажется, в тебя чем-то стрель..")
	input()
	print("ZzZzZ")
	input()
	print("ZzZzZ")
	input()
	print("ZzZzZ")
	input()
	print("ZzZzZ")
	input()
	print("По-моему это конец..")
	input()
	print("Вы мертвы. Нажмите клавишу ENTER для воскрешения на последней точке сохранения")
	input()

def Pogonya():
	print("За тобой погнались охранники. Лучше бы ты был быстрее")
	input()
	print("Ты мог бы свернуть в сторону, но ты и так бежишь по краю")
	input()
	print("Кажется, в тебя чем-то стрель..")
	input()
	print("ZzZzZ")
	input()
	print("ZzZzZ")
	input()
	print("ZzZzZ")
	input()
	print("ZzZzZ")
	input()
	print("По-моему это конец..")
	input()
	print("Вы мертвы. Нажмите клавишу ENTER для воскрешения на последней точке сохранения")
	input()


class Gamee:
	def start():
		opendoorr = 0
		banzai = 0
		colvoGvozd = 0
		zan = 0
		treningg = 0
		zanbar = 0
		player = Character("НоуНейм", 200, 20)
		ambal1tol = Toltol("Амбал1", 100, 20)
		ambal2tol = Tolotos("Амбал2", 100, 20)
		print("Миллионы лет назад началась великая война между людьми и монстрами")
		input()
		print("Мирный договор между рассами не долго сдерживал их ярость")
		input()
		print("Даже самым близким друзьям пришлось воевать друг с другом")
		input()
		print("Жестокое побоище, растратевшая много ресурсов и жизней")
		input()
		print("Из-за людской ярости, люди одержали верх и истребили всех монстров")
		input()
		print("Но никто не говорил, что проблема приходит одна..")
		input()
		print("Загрузка...")
		input()
		print("Загрузка...")
		input()
		print("Загрузка...")
		input()
		print("Загрузка...")
		print("Вы проснулись на кровати в небольшом домике, находящимся в горах")
		input()
		while True:
			try:
				print("Что будешь делать?")
				b = int(input(" Подойти к окну [1] \n Подойти к книжному шкафу [2] \n Поспать [3] \n Выйти в коридор [4]"))
				if b == 1:
					print("В окне виднеются горные холмы, покрытые снегом и сильный снегопад.")
					input()
				if b == 2:
					print("Пустой шкаф, с двумя-тремя валяющимеся в паутине книгами. Прочесть?")
					a = int(input(" да[1] \n нет[2]"))
					if a == 1:
						print("Вы открыли первую попавшуюся книгу, после чего выбрали страницу с закладкой.")
						input()
						print("... начали ожесточённый побоища, КРОВЬ текла рекой, люди, взявшие секиры \n РАЗРУБАЛИ монстров!")
						sa = int(input(" Перелистнуть страницу [1] \n Отойти от шкафа [2]"))
						if sa == 1:
							print("Вы лизнули палец")
							input()
							print("Ваш палец скользит по странице..")
							input()
							print("Лист переворачивается..")
							input()
							print("АААААААААААААААААААА \n ТУТ ИЗОБРАЖЕНИЕ!!! УБЕРИТЕ ЭТУ МЕРЗОООСТЬ!!")
							input()
					if a == 2:
						pass
				if b == 3:
					print("Вы легли в мягкую и удобную постель..")
					input()
					print("ZzZzZzZ")
					input()
					print("ZzZzZzZ")
					input()
					print("ZzZzZzZ")
					input()
					print("ZzZzZzZ")
					input()
					print("ZzZzZzZ")
					input()
					print("ZzZzZzZ")
					input()
					while True:
						print("Вы оказались в странной комнате..")
						son1 = int(input(" Кричать [1] \n Биться об стену [2]"))
						if son1 == 1:
							print("В комнате появилась дверь")
							input()
							print("Вы открывате её..")
							input()
							input()
							input()
							print(" АААААА \n КРОВЬ!! ОНИ СНОВА ЗДЕСЬ!!!")
							input()
							print("Вы вскочили с кровати в холодном поту")
							input()
							break
						if son1 == 2:
							pass
				if b == 4:
					input()
					print("Вы вышли в коридор \n На вешалке висит пальто с железными накладками, в конце коридора дверь")
					input()
					sdas = int(input(" Надеть пальто и выйти из дома[1] \n Вернуться обратно[2]"))
					if sdas == 1:
						print("Вы уверены, что хотите покинуть дом? \n Вы можете многое упустить, не осмотревшись здесь")
						zzx = int(input(" Покинуть дом[1] \n остаться [2]"))
						if zzx == 1:
							print("Зимний горный лес. Интересно, зачем ты здесь?")
							input()
							break
					if sdas == 2:
						pass	
			except ValueError:
				print("Вводить надо цифру! Попробуй сделать это действие снова!")
				input()
		while True:
			print("В далеке виднеется какой-то свет. Приблизиться?")
			try:
				qwe = int(input(" Да [1] \n Нет [2]"))
				if qwe == 1:
					print("Вы подошли ближе, там была яма, из которой бил свет")
					input()
					print("Вам становится плохо")
					input()
					print("Что происходит?")
					input()
					print('"Яма начала светиться интенсивней"')
					input()
					print("Кажется.. ТЕБЯ ЗАСАСЫВАЕТ")
					input()
					print("Ужасная БООЛЬ")
					input()
					print("ПАДАААЕЕМ!!!")
					break
				if qwe == 2:
					pass
			except ValueError:
				print("Вводить надо цифру! Попробуй сделать это действие снова!")
				input()
		try:
			input()
			input()
			print("Играет странная музыка")
			input()
			input()
			print("Мелодия очень простая и жизнерадостная")
			input()
			input()
			print("В глазах по прежнему темно")
			input()
			input()
			print("Яркие цвета")
			input()
			input()
			print("Глаза раскрылись")
			input()
			print("Падение было не смертельным, но ушибы остались")
			input()
			print("Вокруг большой каменный карьер, по середине речка \n Через неё мост к пещере, вокруг деревья")
		except ValueError:
				print("Вводить надо цифру! Попробуй сделать это действие снова!")
				input()
		while True:
			try:
				pohodf = int(input(" Подойти к речке [1] \n Встать на мост [2] \n Осмотреть деревья [3] \n Подойти к пещере [4]"))
				if pohodf == 1:
					print("Река, сомнительно голубого цвета. Рядом валяется удочка с наживкой")
					input()
					print("Порыбачить?")
					ribivi = int(input(" Да [1] \n Нет [2]"))
					if ribivi == 1:
						print("Забрасываем поплавок..")
						while True:
							print("403 * 11 = ?")
							answer = int(input())
							if answer == 4433:
								print("Поплавок начал шататься")
								print("4321 * 2")
								annswer = int(input())
								if annswer == 8642:
									print("Кажется клюёт!")
									print("841 : 5")
									annnswer = int(input())
									if annnswer == 168:
										print("КЛЮЁТ! ВЫТЯГИВАЙ!!")
										input()
										print("Вы поймали рыбу, она была добавлена в ваш инвентарь.")
										playerInventory["Сырая рыба"] = "Конечно и генерирует здоровье, но всё-таки лучше её пожарить. При поедании +20 к здоровью	  "
										break
									if annnswer != 168:
										print("Ну нееет.. Мимо.. Попробуй ещё раз")
								if annswer != 8642:
									print("Ну нееет.. Мимо.. Попробуй ещё раз")
							if answer != 4433:
								print("Ну нееет.. Мимо.. Попробуй ещё раз")
					if ribivi == 2:
						print("Как хочешь")
						input()
				if pohodf == 2:
					print("Мост сделан из тёмного дерева")
					input()
					print("Скорее всего, он не очень прочный")
					input()
					if colvoGvozd == 0:
						print("На полу лежит гвоздь. Взять?")
						viboriri = int(input(" Да [1] \n Нет [2]"))
						if viboriri == 1:
							print("Гвоздь добавлен в ваш инвентарь")
							playerInventory["Гвоздь"] = "Довольно-таки острый"
							colvoGvozd += 1
							input()
					if colvoGvozd > 0:
						pass
				if pohodf == 3:
					print("На первый взгляд обычные деревья")
					input()
					print("Но у них голубая листва")
					input()
					sbor = int(input(" Попытаться оторвать ветку [1] \n Вернуться обратно [2]"))
					if sbor == 1:
						print("Не получилось.. Придётся уходить..")
						input()
						print("БАМ!")
						input()
						print("Вам на голову упала ветка")
						input()
						print("Ветка добавлена в инвентарь")
						playerInventory["Странная ветка.."] = "Впервые вижу такую.."
						input()
					if sbor == 2:
						pass
				if pohodf == 4:
					print("Глубокая.. И тёмная..")
					input()
					print("Войти?")
					vhodof = int(input(" Да [1] \n Нет [2]"))
					if vhodof == 1:
						print("Заходим..")
						input()
						input()
						input()
						print("Яркий свет в конце туннеля..")
						input()
						input()
						input()
						print("Глаза слепит..")
						input()
						input()
						input()
						break
			except ValueError:
				print("Вводить надо цифру! Попробуй сделать это действие снова!")
				input()
		input()
		input()
		print(" Достижение разблокировано \n Чужой среди своих")
		input()
		print("Вы вышли из туннеля")
		input()
		print( """         ЭТО ПРЕКРАСНО!! ВОКРУГ ВАС ГИГАНТСКИЙ КАРЬЕР, ПОДНИМАЮЩИЙСЯ ВВЕРХ
			ПО СТУПЕНЯМ!! КУЧУ ЭТАЖЕЙ, ЗДАНИЙ, ВЫСЕЧЕННЫХ ИЗ КАМНЯ И ДРУГИХ МАТЕРИАЛОВ,
			ПО ВСЮДУ КА.. какие-то странные.. мон.. стры.. да.. Не может быть!! Их же.. истребили!!""")
		input()
		print("Вы ужасно напуганы")
		input()
		print("Вы стоите перед входом в этот чудный город, перед вами шлагбаум и двое охранников - монстров")
		input()
		print("Чекпоинт!")
		while True:
			try:
				dogs = int(input(" Рвануться в сторону и убежать [1] \n Побежать назад [2] \n Подойти к шлагбауму [3]"))
				if dogs == 1:
					Pogonya()
				if dogs == 2:
					Pogonya()
				if dogs == 3:
					break
			except ValueError:
				print("Вводить надо цифру! Попробуй сделать это действие снова!")
				input()
		print("Вы подошли к пропускному пункту. Около шлагбаума будка")
		input()
		print("Из будки вышли два антропоморфных пса")
		input()
		print("Один гигантский пёс подошёл и грозно встал перед вами")
		input()
		input()
		print("По вам течёт пот")
		input()
		input()
		print("Его грозное лицо нависло над вами, а секира за спиной пугает своими размерами")
		input()
		input()
		print("Он широко раскрыл пасть, вы видете его заострённые зубы и ужасно агрессивное лицо")
		input()
		input()
		print("Он.. Начинает.. Говорить..")
		input()
		input()
		print("Тяф!")
		while True:
			try:
				dszx = int(input(" Рассмеяться[1] \n Промолчать[2]"))
				print("Из будки вышел ещё один пёс, но примерно вашего роста")
				input()
				print("Малый пёс: Приветствую, с какой целью пришёл?")
				input("Опиши, зачем ты здесь?")
				print("Малый пёс: Извини, но наш создатель не настолько умён, чтобы я мог понять тебя. \n Просто.. Просто давай сделаем вид, что я тебя понял")
				input()
				print("Малый пёс: Проходи")
				input('"Шлагбаум открылся"')
				aosko = int(input(" Спросить о том, как  он смог поверить в то, что ты монстр [1] \n Ничего не спрашивать [2]"))
				if aosko == 1:
					print("Малый пёс: По твоему уродливому лицу")
					input()
					print("Это было обидно.")
					input()
					input()
					input()
				if aosko == 2:
					print("Тогда, идём дальше")
					input()
					input()
					input()
				print("Вот ты и внутри этого города. Ты находишься на первом этаже, с каждым этажом площадь города расширяется \n Ты сейчас на этаже уровня 0. Вокруг тебя мало объектов \n Попробуй осмотреться, может узнаешь, как монстры смогли выжить \n или как выбраться отсюда")
				input()
				break
			except ValueError:
				print("Вводить надо цифру! Попробуй сделать это действие снова!")

		while True:
			print("Куда отправимся?")
			try:
				urokii = int(input(" В старое монашеское здание, виднеющееся в далеке [1] \n В кузницу, находящуюся в 20 метрах [2] \n К толпе народа, хотя нет, монстронарода, которая что-то обсуждает [3] \n В здание, напоминающее банк [4] \n На ступени для подъёма на второй этаж [5]"))
				input()
			except ValueError:
				print("Вводить надо цифру! Попробуй сделать это действие снова!")
			except UnboundLocal:
				pass
			if urokii == 1:
					print("Вы вошли в здание, вокруг лежат маты, на стене гонг \n в комнате есть три двери.")
					while True:
						try:
							muzgj = int(input(" Войти в первую дверь [1] \n Войти во вторую дверь [2] \n Войти в третью дверь [3] \n Уйти отсюда [4]"))
							if muzgj == 1:
								if banzai == 0:
									print("Вы вошли, это был мужской туалет")
									input()
									print("В углу вы видете, как двое амбалов избивают несчастного монстрика")
									input()
									if zan == 0:
										print("Вас заметили амбалы и вышвырнули за дверь, после чего заперли её")
										input()
										bitka = int(input("Попытаться выломать дверь [1] \n Уйти отсюда [2]"))
										if bitka == 1:
											print("Амбал1: Пха! Не сможешь, силёнки не достаточно!")
											input()
											break
										if bitka == 2:
											print("Выходим..")
											input()
											break
									if zan == 1:
										print("Вас заметили амбалы и вышвырнули за дверь, после чего заперли её")
										input()
										bitka = int(input("Попытаться выломать дверь [1] \n Уйти отсюда [2]"))
										if bitka == 1:
											print("Вы успешно выломали дверь")
											input()
											print("Амбал 1 побежал на вас")
											input()
											print("Битва!")
											while True:
												print("Амбал1 грозно смотрит на вас")
												atakyi = int(input(" Обычные удары [1] \n Заклинания [2] \n Боевое исскуство монстров [3]"))
												if atakyi == 2:
													print("Вы ещё не изучили ни одного заклинания")
													input()
												if atakyi == 3:
													print("Вы ещё не изучили это боевое исскуство")
												if atakyi == 1:
													sablas1 = int(input(" Удар саблей [1] \n Удар напролом [2] \n"))
													if sablas1 == 1:
														player.attackbaz(ambal1tol)
														input()
													if sablas1 == 2:
														print("Вы ещё не изучили этот приём")
														input()
													ambal1tol.ambalattack(player)
													if ambal1tol.hp <= 0:
														print("Ты.. Ты одолел их!")
														player.hp += 200
														if player.hp > 200:
															player.hp = 200
															print("Здоровье восстановлено")
														input()
														print("Маленький избитый монстрик подбегает к тебе")
														input()
														print("Монстрик: Спасибо, дяденька!")
														input()
														print("Монстрик убежал, дав вам какую-то монету")
														banzai += 1
														opendoorr += 1
														break
																	
								if banzai == 1:
									print("Пустой мужской туалет. Ничего удивительного")
									input()
							if muzgj == 2:
								print("Вы вошли, это был женский туалет")
								input()
								print("Пожалуй выйдем отсюда")
								input()
								print("После твоего ухода было слышно, что дверь была заперта")
								input()
								break
							if muzgj == 3:
								print("Вы вошли.")
								input()
								print("Вокруг было пусто по середине комнаты мат на котором сидел монстр")
								input()
								print("Тренер: Здраствуй, пришёл обучиться боевому исскуству?")
								isskus = int(input(" Да [1] \n Нет [2]"))
								if isskus == 2:
									print("Тренер: Ну.. Поступай как знаешь..")
									input()
									break
								if isskus == 1:
									print("Тренер, Пхе, ну не за бесплатно ведь мне тебя учить")
									shafz = int(input(" У меня нет денег [1] \n Уйти [2] \n Спросить о том, как монстры смогли выжить [3]"))
									if shafz == 1:
										print("Тренер: Ну.. Первое занятие я могу провести бесплатно")
										input()
										print("Тренер: Однако научу я тебя за бесплатно обучу только фехтованию")
										input()
										print("Тренер: Начнём")
										input()
										input()
										input()
										print(" Достижение разблокировано \n Юный боец")
										input()
										input()
										input()
										print(" Тренер: Фехтование зависит от твоего выбора атака должна быть \n блестящей и напористой, а защита - хитрой и коварной.")
										input()
										print("Тренер: Чем точнее и исскустнее твои приёмы, тем хуже для противника")
										input()
										print("Тренер: Следи за тем, что вытворяет оппонент, если хочешь его одолеть")
										input()
										print("Тренер: Крит урон - это твой урон, умноженный на два")
										input()
										print("Тренер: А, ещё, чтобы сломать дверь, нужно всё усилие сконцентрировать в ноге")
										input()
										zan += 1
										treningg += 1
										break
									if shafz == 2:
										print("Тренер: Ну.. Поступай как знаешь..")
										input()
										break
									if shafz == 3:
										Chelovek()
							if muzgj == 4:
								print("Выходим..")
								input()
						except ValueError:
							print("Вводить надо цифру! Попробуй сделать это действие снова!")
			if urokii == 2:
					input()
					print("Дверь заперта. Требуется ключ")
					input()
			if urokii == 3:
					input()
					print("Вы подошли к толпе, это была очередь, интересно, куда?")
					input()
					try:
						otvertnador = int(input(" Спросить о том, как монстры смогли выжить [1] \n Уйти отсюда [2]"))
						if otvertnador == 1:
							Chelovek()
						if otvertnador == 2:
							print("Уходим..")
							input()
					except ValueError:
						print("Вводить надо цифру! Попробуй сделать это действие снова!")
			if urokii == 4:
					input()
					print("Вы зашли в банк, на кассе стоит монстр")
					input()
					while True:
						try:
							bankoer = int(input(" Узнать о функциях банка [1] \n Просмотреть свои вещи [2] \n Узнать о том, как монстры смогли выжить [3] \n Уйти отсюда [4]"))
							if bankoer == 1:
								input()
								print("Банкир: В банке ты можешь осмотреть свой инвентарь и узнать описание предметов")
								input()
								print("Ты: Почему только в банке?")
								input()
								print("Банкир: По-моему ты задаёшь слишком много вопросов")
								input()
							if bankoer == 2:
								input()
								OpenInventory()
							if bankoer == 3:
								Chelovek()
							if bankoer == 4:
								print("Уходим..")
								input()
								break
						except ValueError:
							print("Вводить надо цифру! Попробуй сделать это действие снова!")
			if urokii == 5:
					if opendoorr == 1:
						input()
						print("Эта лестница ведёт на второй этаж. Заходим?")
						try:
							naw = int(input(" Да [1] \n Нет [2]"))
							if naw == 1:
								print("Всё")
								input()
								print("Конец")
								input()
								print("Вернее, это не должен был быть конец")
								input()
								print("У меня были на эту игру огромные планы")
								input()
								print("Я хотел сделать ещё много-много этажей, который можно исследовать")
								input()
								print("Путешествовать и сражаться с противниками")
								input()
								print("Но, к сожалению, сроки поджимают..")
								input()
								print("И это всё, что я успел сделать к пятнице")
								input()
								input()
								print("Поэтому, давай воспримем это, как демо-версию")
								input()
								print("Спасибо за игру.")
								input()
								input()
								raise KonetzError
							
						except ValueError:
							print("Вводить надо цифру! Попробуй сделать это действие снова!")
						if naw == 2:
							input()
							print("Ну, как знаешь..")
							input()
					if opendoorr != 1:
						input()
						print("Тебе нужна специальная монетка!")
						input()
Gamee.start()