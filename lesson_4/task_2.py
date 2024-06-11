k = str(input("Введите строку : "))
vowels = 'aаAА'
counter  = 0
for letter in k:
    if letter in vowels:
         counter += 1

print(counter)
