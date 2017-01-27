word = input("Введите слово ")
# res = word[-1::-1]
# res = word[len(word)//2:] + word[0:len(word)//2]
res = word.lower().replace('а','б').replace('о','у')
print(res)
