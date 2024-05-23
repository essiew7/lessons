def even_square(data):
    data = [k**2 for k in data if k % 2 == 0]
    print(data)
    data = sum(data)
    print(data)

a = [x for x in range(1,11)]
even_square(a)