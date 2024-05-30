from itertools import permutations


def possible_comb(nums_list):
    for i in permutations(nums_list):
        yield i


a = [1, 2, 5]
for k in possible_comb(a):
    print(k)
