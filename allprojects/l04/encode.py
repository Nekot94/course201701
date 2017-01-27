word = input("Введите строку: ")
# print(word[-1::-1])
# res = word[len(word)//2:] + word[0:len(word)//2]
# print(res)
res = word.replace("а","в").replace("о","у")
print(res)
