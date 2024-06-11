a, b = int(input("a = : ")), int(input("b = : "))
squares = [x for x in range(a,b+1) if x % 2 == 0 ]
print(squares)