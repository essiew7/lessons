def num_check(data):
    data = [k for k in data if k & k-1 == 0 and k!= 1]
    print(data)

a = [1, 2, 4, 8, 10, 16, 25, 32, 88, 64]
num_check(a)