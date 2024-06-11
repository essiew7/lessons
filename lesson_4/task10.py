word = str(input("Введите слово : "))
a = 'aA'
for symbols in a:
    word = word.replace(symbols,"")
print(word)
