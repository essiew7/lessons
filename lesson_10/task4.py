def list_nums_square(nums_list):
    squared_list = list(map(lambda x: x ** 2, nums_list))
    return squared_list

a = [1, 16, 12, 4, 2]
print(list_nums_square(a))