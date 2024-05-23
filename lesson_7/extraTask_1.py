def numbers3_check(a):
    one = a // 100
    two = a % 11
    three = a % 10
    numbers_list = [one,two,three]
    numbers_list = [k**2 for k in numbers_list]
    print(sum(numbers_list))

a = 321
numbers3_check(a)