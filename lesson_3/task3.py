number = str(input("Введите число : "))
num1, num2 = number*2, number*3
num1, num2, number = int(num1), int(num2), int(number)
print(f"Итоговая сумма равна {number+num1+num2}")