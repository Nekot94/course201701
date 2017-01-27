import random
a = random.randint(1,10)
print("4 *",a,"=") 
# print("4*" + str(a) + "=")
answer = int(input())
if answer ==  4 * a:
    pnrint("правильно")
else:
    print("неправильно")