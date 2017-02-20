# f1 = open("lalka.txt","wt", encoding="utf-8")
# f1.write("Azazaz\n")
# f1.write("Арсен любит котико\n")
# print("Ты серьезен?", file=f1)
# f1.close()

# f2 = open("lalka.txt", "rt", encoding="utf-8")
# text = f2.read(30)
# f2.close()
# print(text)


# f2 = open("lalka.txt", "rt", encoding="utf-8")
# text = f2.readline()
# text2 = f2.readline()
# f2.close()
# print(text + text2)


# f2 = open("lalka.txt", "rt", encoding="utf-8")
# for line in f2:
# 	print(line[:-1])
# f2.close()

# text = """Бейте смелых друзей,
# Усладят нас смелых кукушек"""

# with open("best_poem.txt", 'wt', encoding="utf-8") as f1:
# 	f1.write(text)

# with open("best_poem.txt", 'at', encoding="utf-8") as f1:
# 	f1.write("\nкукушек кукушек друзей")

with open("best_poem2.txt", 'rt', encoding="utf-8") as f1:
	print(f1.read())




