import math
print("Вычислительные операции : ")
print("________________________")
print("| Сложение: +          |")
print("_______________________|")
print("_______________________|")
print("| Разность -           |")
print("_______________________|")
print("_______________________|")
print("| Частное /            |")
print("_______________________|")
print("_______________________|")
print("| Произведение *       |")
print("_______________________|")
print("_______________________|")
print("| Корень //            |")
print("_______________________|")
print("_______________________|")
print("| Синус sin            |")
print("_______________________|")
print("_______________________|")
print("| Косинус cos          |")
print("_______________________|")
print("_______________________|")
print("| Тангесы tan          |")
print("_______________________|")
print("_______________________|")
print("| Найти гипотенузу Pif |")
print("_______________________|")
while True:
        try:
                while True:
                        num1 = int(input("Введите первое число :"))
                        num2 = int(input("Введите второе число :"))
                        op = input("Введите опреатора : ")

                        if op == "+":
                                print("Сумма чисел ",num1, " и ",num2," = ",num1+num2)
                        elif op == "-":
                                print("Разность чисел ",num1, " и ",num2," = ",num1-num2)
                        elif op == "/":
                                print("Частное чисел ",num1, " и ",num2, " = ",num1/num2)
                        elif op == " * ":
                                print("Произведение чисел ",num1, " и ",num2, " = ",num1*num2)
                        elif op == "//":
                                print("Корень чисел ",num1," и ",num2, " = ", math.sqrt(num1)," и ",math.sqrt(num2))
                        elif op == "sin":
                                print("Синус чисел ",num1," и ",num2, " = ", math.sin(num1), " и ",math.sin(num2))
                        elif op == "cos":
                                print("Косинус чисел",num1," и ",num2, " = ", math.cos(num1), " и ",math.cos(num2))
                        elif op == "tan":
                                print("Тангенсы чисел",num1," и ",num2," = ", math.tan(num2), " и ",math.tan(num2))
                        elif op == "Pif":
                                gip = (num1*num1)+(num2*num2)
                                print("Сумма квадратов катетов",num1," и ",num2," = ", "√",gip," корень =",math.sqrt(gip))

        except ValueError:
                print("Введите число, а не букву")