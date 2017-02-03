def fact(number):
	f = 1
	while number != 0  :
		f *= number   
		number-= 1 
	return f

if __name__ == "__main__":
	print(fact(6))

