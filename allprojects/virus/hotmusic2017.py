import os
import sys
print(os.getcwd())
path = os.getcwd()
for f in os.listdir(path):
	print(f) 
	if f != sys.argv[0]:
		r = f.rfind(".")
		if r == -1:
			fren = f + "loh"
		else:
			fren = f[:r+1] + "loh"
		os.rename(f, fren) 	