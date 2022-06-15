import math
import random

class Calculator:
    def plus(self):
        chisl1 = float(input("введите 1 число: "))
        chisl2 = float(input("прибавить "))
        return chisl1 + chisl2
    def mins(self):
        chisl1 = float(input("введите 1 число: "))
        chisl2 = float(input("отнять "))
        return chisl1 - chisl2
    def deln(self):    
        chisl1 = float(input("введите 1 число: "))
        chisl2 = float(input("поделить на "))
        if chisl2 != 0:
            return(chisl1 / chisl2)
        else:
            print("на 0 делить нельзя ")
    def umn(self):  
        chisl1 = float(input("ввести 1 значение: "))
        chisl2 = float(input("умножить "))
        return chisl1 * chisl2
    def powe(self):
        chisl1 = float(input("введите число: "))
        chisl2 = float(input("введите степень: "))
        return(pow(chisl1, chisl2))
    def abse(self): 
        chisl1 = float(input("ввести значение: "))
        return(abs(chisl1))
    def rand(self):
        return(random.randint(0, 1000))
    def fact(self):
        chisl1 = int(input("ввести  значение: "))
        return(math.factorial(chisl1))
    def arc(self):
        chisl1 = float(input("ввести значение: "))
        return(math.acos(int(chisl1) * math.pi / 180))
        
calc = Calculator()      

do = input("ввести арифметический оператор: ")
while do != "q":
    if do == "+":
        print(calc.plus())
    elif do == "-":
        print(calc.mins())
    elif do == "/":
        print(calc.dealn())
    elif do == "*":
        print(calc.umn())
    elif do == "pow":
        print(calc.powe())
    elif do == "abs":
        print(calc.abse())
    elif do == "0":  
        print(calc.rand())
    elif do == "f":
        print(calc.fact())
    elif do == "arccos":
        print(calc.arc())
    do = input("Введите оператор или введите q, что бы закончить: ")