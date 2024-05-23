import math
a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))
print(f"Наименьшее общее кратное = ",int(a*b/math.gcd(a,b)))