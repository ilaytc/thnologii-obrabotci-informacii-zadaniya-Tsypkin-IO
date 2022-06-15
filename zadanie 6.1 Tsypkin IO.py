import math
import random
def plus():
    chisl1 = float(input("введите 1 число: "))
    chisl2 = float(input("прибавить "))
    return chisl1 + chisl2
def mins():
    chisl1 = float(input("введите 1 число: "))
    chisl2 = float(input("отнять "))
    return chisl1 - chisl2
def deln():    
    chisl1 = float(input("введите 1 число: "))
    chisl2 = float(input("поделить на "))
    if chisl2 != 0:
        return(chisl1 / chisl2)
    else:
        print("на 0 делить нельзя ")
def umn():  
    chisl1 = float(input("ввести 1 значение: "))
    chisl2 = float(input("умножить "))
    return chisl1 * chisl2
def powe():
    chisl1 = float(input("введите число: "))
    chisl2 = float(input("введите степень: "))
    return(pow(chisl1, chisl2))
def abse(): 
    chisl1 = float(input("ввести значение: "))
    return(abs(chisl1))
def rand():
    return(random.randint(0, 1000))
def fact():
    chisl1 = int(input("ввести  значение: "))
    return(math.factorial(chisl1))
def arc():
    chisl1 = float(input("ввести значение: "))
    return(math.acos(int(chisl1) * math.pi / 180))
do = input("ввести арифметический оператор: ")
while do != "q":
    if do == "+":
        print(plus())
    elif do == "-":
        print(mins())
    elif do == "/":
        print(dealn())
    elif do == "*":
        print(umn())
    elif do == "pow":
        print(powe())
    elif do == "abs":
        print(abse())
    elif do == "0":  
        print(rand())
    elif do == "f":
        print(fact())
    elif do == "arccos":
        print(arc())
    do = input("Введите оператор или введите q, что бы закончить: ")