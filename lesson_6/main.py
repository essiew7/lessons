s = int(input("Введите число : "))
a = [x for x in range(1,s+1)]
print(a)
b = [square ** 2 for square in a]
print("квадраты чисел",b)
c = [x % 11 for x in a ]
print("остаток от деления на 11",c)
d = [x for x in a if x % 2 == 0]
print("только четные",d)
e = [x for x in a if x % 2 != 0]
print("нечетные",e)
f = [x for x in a if x>= 10 for c in range(2)]
print("2-ух значные элементы записанные 2 раза подряд",f)
d = [x for x in a if x%3 != 0 ]
print("числа не кратные 3",d)
