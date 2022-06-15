stro = input("vvedite predlogenie ")
for x in range(0, len(stro)):
    if x != 2:
        print(stro[x])
if stro.find("с") >= 0:
    print("est с")
print(len(stro))
print(stro[:len(stro) - 1])