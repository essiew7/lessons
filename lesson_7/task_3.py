def even_check(data):
    data = [x for x in data if x % 2 == 0]
    print(data)

a = [k for k in range(1,11)]
even_check(a)