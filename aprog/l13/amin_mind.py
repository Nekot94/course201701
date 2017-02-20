import os
variables = {"NULL" : 0}


def fsc(stroka):
		name = stroka[0:stroka.find(" ")]
		arg = stroka[stroka.find(" ")+1:len(stroka)]
		args = arg.split(" ")
		if name == "addstr":
			variables[args[0]] = args[1]
		if name == "addint":
			variables[args[0]] = int(args[1])
		if name == "summa":
			a = int()
			b = int()
			if args[1] in variables :
				a = variables[args[1]]
			else:
				a = int(args[1])
			if args[2] in variables :
				b = variables[args[2]]
			else:
				b = int(args[2])
			variables[args[0]] = a+b
		if name == "vrblout":
			print(variables[arg])
		if name == "raznost":
			a = int()
			b = int()
			if args[1] in variables :
				a = variables[args[1]]
			else:
				a = int(args[1])
			if args[2] in variables :
				b = variables[args[2]]
			else:
				b = int(args[2])
			variables[args[0]] = a-b
		if name == "umn":
			a = int()
			b = int()
			if args[1] in variables :
				a = variables[args[1]]
			else:
				a = int(args[1])
			if args[2] in variables :
				b = variables[args[2]]
			else:
				b = int(args[2])
			variables[args[0]] = a*b
		if name == "delit":
			a = int()
			b = int()
			if args[1] in variables :
				a = variables[args[1]]
			else:
				a = int(args[1])
			if args[2] in variables :
				b = variables[args[2]]
			else:
				b = int(args[2])
			variables[args[0]] = a+b
		if name == "summstr":
			a = str()
			b = str()
			if args[1] in variables :
				a = variables[args[1]]
			else:
				a = int(args[1])
			if args[2] in variables :
				b = variables[args[2]]
			else:
				b = int(args[2])
			variables[args[0]] = a+b
		if name == "equals":
			variables[args[0]] = args[1] == args[2]
		if name == "biggest":
			variables[args[0]] = args[1] > args[2]
		if name == "menshe":
			variables[args[0]] = args[1] > args[2]
		if name == "addNSC" :
			variables[args[0]] = args[1:]
		if name == "addNIC":
			res = list()
			for n in range(1,len(args[1:])+1):
				res.append(int(args[n]))
			variables[args[0]] = res
		if name == "totalString":
			res = ""
			for kankutationelem in variables[args[1]]:
				res += kankutationelem
			variables[args[0]] = res
		if name == "nullizateNSC":
			for n in variables[arg]:
				variables[arg][n] = ""
		if name == "nullizateNIC":
			for n in variables[arg]:
				variables[arg][n] = 0
		if name == "totalInt":
			res = 0
			for kankutationelem in variables[args[1]]:
				res += kankutationelem
			variables[args[0]] = res
		# if name == "addfunc":
		# 	fname = args[0]

		# if name == "repeat":
		# 	for 


while True:
	cnd = input()
	fsc(cnd)