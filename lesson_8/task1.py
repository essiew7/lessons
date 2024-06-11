a = input("введите число : ")
b = [k for k in a ]
f, t = bool, bool
numbers = ["1", "2", "3", "4", "5"]
for k in b:
    if str(k) not in numbers:
        f = False
    else: t = True
if f == False: print("not special")
else: print("special")