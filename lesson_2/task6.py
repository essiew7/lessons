word = input("Введите слово : ")

a = 1
for c in word:
    if word.count(c)>1:  a = 0

if a == 1:
    print("Слово является изограммой")
else:print("Слово не является изограммой")