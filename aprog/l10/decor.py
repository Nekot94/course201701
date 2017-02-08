# def show_em_all(func):

# 	def wrapper(*args, **kwargs):
# 		print("Название функции:", func.__name__)
# 		print("Позиционные аргументы:", args)
# 		print("Именованные аргументы:", kwargs)
# 		result = func(*args, **kwargs)
# 		print("Результат", result)
# 		return result

# 	return wrapper

# # def summ6(a,b):
# # 	return (a + b) * 6

# # @show_em_all
# # def loh_you(name):
# # 	print(name +", поздравляю ты лох")

# # nice_summ6 = show_em_all(summ6)
# # print(summ6(5,5))
# # print(nice_summ6(6,6))
# # # show_em_all(loh_you)("еюеххи")
# # loh_you("Камид")

# def no(func):

# 	def wrapper(*args, **kwargs):
# 		return str(func(*args, **kwargs)) + "(НЕТ)"
# 	return wrapper		


# @no
# @show_em_all
# def you_pretty(name):
# 	return name + " - красавчик"

# print(you_pretty("Камал"))

super_funce = lambda a, b: a + " " + b + " Амин"

print(super_funce("Мир","Труд"))

good_boys = ["Аслан","арслан","Джавилито","саид-посигнувший"]

good_boys.sort(key=lambda e: e.lower())


print(good_boys)


