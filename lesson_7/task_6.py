def range_check(data):
    data = [k for k in data if k < 20 and k > 10]
    print(data)

a = [k for k in range(1,25)]
range_check(a)