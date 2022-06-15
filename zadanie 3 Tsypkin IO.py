import math
import random
do = input("ввести арифметический оператор: ")
while do != "q":
    if do == "+":
        chisl1 = float(input("введите 1 число: "))
        chisl2 = float(input("прибавить "))
        print(chisl1 + chisl2)
    elif do == "-":
        chisl1 = float(input("введите 1 число: "))
        chisl2 = float(input("отнять "))
        print(chisl1 - chisl2)
    elif do == "/":
        chisl1 = float(input("введите 1 число: "))
        chisl2 = float(input("поделить на "))
        if chisl2 != 0:
            print(chisl1 / chisl2)
        else:
            print("на 0 делить нельзя ")
    elif do == "*":
        chisl1 = float(input("ввести 1 значение: "))
        chisl2 = float(input("умножить "))
        print(chisl1 * chisl2)
    elif do == "pow":
        chisl1 = float(input("введите число: "))
        chisl2 = float(input("введите степень: "))
        print(pow(chisl1, chisl2))
    elif do == "abs":
        chisl1 = float(input("ввести значение: "))
        print(abs(chisl1))
    elif do == "0":  
        print(random.randint(0, 1000))
    elif do == "f":
        chisl1 = int(input("ввести  значение: "))
        print(math.factorial(chisl1))
    elif do == "arccos":
        chisl1 = float(input("ввести значение: "))
        print(math.acos(int(chisl1) * math.pi / 180))
    do = input("Введите оператор или введите q, что бы закончить: ")