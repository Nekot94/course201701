import random
name = "зов ктулху.txt"
with open(name, "rt", encoding="utf-8") as f:
	text = f.read()
# print(text)я
input ("Введите вопрос: ") 
edd = 50
random_number = random.randint(1,len(text)-30)
answer = text[random_number:random_number+edd]
start = answer.find(" ")
stop = answer.rfind(" ")
answer = answer[start + 1:stop]
print(answer)

