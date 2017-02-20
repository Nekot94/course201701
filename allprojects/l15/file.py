with open("дохлая кошка.txt","w", encoding="utf-8") as file:
	file.write("Арсен держит в руке дохлую кошку")
with open("дохлая кошка.txt","r",encoding="utf-8") as file:
	text=file.read(10)
print(text)