from math import sqrt
def IsSimpleNumb(number) -> bool:
    if number == "exit": exit(0)
    number = int(number)
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    number = int(number)
    number = int(sqrt(number))
    for k in range(3,number,2):
        if number % k == 0:
            return False
    return True
while(True):
    pomidor = input()
    tomato = IsSimpleNumb(pomidor)
    print(tomato)