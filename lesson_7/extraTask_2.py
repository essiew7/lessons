def numbers_sort(data):
    even = [k for k in data if k % 2 == 0]
    odd = [k for k in data if k % 2 != 0]
    result = even + odd
    print(result)

a = [k for k in range(1,10)]
numbers_sort(a)