word = ["Иса","Арсен","Магомед"]
print(word)
word.append("Магомедрасул")
print(word)
word.remove("Магомедрасул")
print(word)
word.pop(0)
print(word)
word.insert(2,"Сайка")
string = " <3 ".join(word)
print(string)
print(string.split("а"))
number = 3,2,1
print(number)
numbers = {1,2,1,3,"Иса"}
print(numbers)

ru_eng_dict = {
"яйцо":"egg",
"клавиатура":"keyboard",
"лох":"looser"
}
print(ru_eng_dict["клавиатура"])
ru_eng_dict["лох"] = "goof"
print(ru_eng_dict)
ru_eng_dict["Иса"] = "Isaac"
print(ru_eng_dict)



