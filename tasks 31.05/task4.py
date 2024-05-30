from random import choice


def gen_random_num(a,b):
    a = choice(range(a,b+1))
    yield a


for k in gen_random_num(100,100000):
     print(k)