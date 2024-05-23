def str_len(str_list):
    str_list = [x for x in str_list if len(x) > 5]
    print(str_list)

a = ['dsadas', 'asd', 'asda', '666666', 'dipjsoafg']
str_len(a)