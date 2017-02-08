# def show_all(func):
# 	def wrapper(*args, **kwargs):
# 		print("Имя нашей функции:", func.__name__)
# 		print("Позиционные аргументы:", args)
# 		print("Именованные аргументы:", kwargs)
# 		result = func(*args,**kwargs)
# 		print("Результат:", result)
# 		return result
# 	return wrapper

# def summ5(x,y):
# 	return (x+y)*5


# def beauty(me):
# 	print(me ,"красавчик")

# @show_all
# def beauty2(me):
# 	print(me ,"кр2савчик")

# summ5_beauty = show_all(summ5)

# summ5_beauty(5,6)

# show_all(beauty)("Гамид")

# beauty2(me="Гамид")



def no(fat):
	def wrapper(*args, **kwargs):
		return str(fat(*args, **kwargs)) +"(нет)"
	return wrapper


@no
def beauty3(me):
	return me +" красавчик"

def last_sort(e):
	return e[-1]

print(beauty3("hbarskfghskughau"))


print((lambda me: me +" красавчик")("123")) 

good_boys = ["рустам", "Гаджи", "Саид", "иса"]

good_boys.sort(key = lambda e: e.lower())
# good_boys.sort(key = lambda e: e[-1])
good_boys.sort(key=last_sort)
print(good_boys)
