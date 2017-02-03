# import random
# print(random.randint(1,3))
from random import choice
lohy = ["Магомедрасул", "Абдул", "Гаджимурад"]
print("Сейчас умрет",choice(lohy))
# from math import cos, sqrt, pi

# print(cos(pi))
# print(sqrt(4))
from math import *

print(ceil(6.7))

import factorial

print(factorial.fact(7))

from os import remove, listdir
# remove("idioto.txt")
print(listdir("."))

import sys

if len(sys.argv) >= 3:
	print(int(sys.argv[1]) + int(sys.argv[2]))

# from datetime import time

# print(time())

import time

while True:
	time.sleep(3)
	print(floor(time.clock()))
	if floor(time.clock()) == 9:
		print("Не ждали")
		break


