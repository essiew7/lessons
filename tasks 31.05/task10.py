from itertools import permutations


def possible_password(symbols_list,pass_range):
    for k in permutations(symbols_list,pass_range):
        yield k



a = ["j",'5',"8","$","s"]
for k in possible_password(a,2):
    print(k)


