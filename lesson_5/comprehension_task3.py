a = input("Введите строку : ")
vowels = 'уеыаоэяиюeyuioa'
output = [letter for letter in a if letter in vowels]
print(output)