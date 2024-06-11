a, b = int(input("a = : ")), int(input("b = : "))
squares = [x**2 for x in range(a,b+1)]
print(squares)