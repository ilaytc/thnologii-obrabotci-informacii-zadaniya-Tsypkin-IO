sp1 = input("введите список слов через запятую: ")
sp1 = sp1.split(",")
chisl1 = len(sp1)
print("в списке {} слов".format(chisl1))
sp2 = input("ведите 2 список из {} слов через запятую: ".format(chisl1))
sp2 = sp2.split(",")
slov = dict(zip(sp1, sp2))
print(slov)