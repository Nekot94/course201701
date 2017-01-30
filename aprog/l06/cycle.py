a = -1
while a < 10:
	a +=1
	if a == 7:
		continue
	print (a)
	
friends = {"Мирвет": 13, "Илья": 15, "Саид": 26}
for key, value in friends.items(): 
	print("Моего друга зовут",key,"ему",value)

for i in range(10,1,-1):
	print(i)