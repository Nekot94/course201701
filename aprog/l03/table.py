import random
random_number = random.randint(1,10)
# print(random_number)
print("2 *",random_number,"=")
answer = int(input())
if answer == 2 * random_number:
    print ("правильно")
else:
    print("неправильно")

