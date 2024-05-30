from itertools import permutations


def possible_comb(letter_str):
    yield letter_str
    letter_list = [k for k in letter_str]
    for i in permutations(letter_list):
        yield i


a = "asd"
for k in possible_comb(a):
    print(k)
