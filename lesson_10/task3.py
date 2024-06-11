def str_len(a):
    new_list = list(filter(lambda x: (len(x) > 3), a))
    return new_list


a = ["время", "дуб", "скобка", "python", "яд"]
print(str_len(a))