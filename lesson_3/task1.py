num = int(input("Введите двухзначное число : "))
if num >= 100 or num < 10: print('Ошибка! Значение числа должно быть в диапазоне от 10 до 99'), exit(0)
num2 = num % 10
num1 = int(num / 10)
if num1 == num2:
    print(f'Да, число {num} состоит из одинаковых цифр')
else:
    print(f'Нет, число {num} не состоит из одинаковых цифр')