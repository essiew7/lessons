def endwith_o(num_list):
    new_list = list(filter(lambda word: word.lower().endswith('o') or word.lower().endswith('о'),num_list))
    return new_list


a = ['ящерица', 'окно', 'potato', 'winter']
print(endwith_o(a))
