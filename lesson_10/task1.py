def list_even(array):
    even_list = list(filter(lambda x: (x % 2 == 0),array))
    return even_list

a = [k for k in range(1,15)]
print(list_even(a))