from random import choice


def gen_random_color():
    r = choice(range(1, 256))
    g = choice(range(1, 256))
    b = choice(range(1, 256))
    dictionary = {"red": r, "green": g, "black": b}
    yield dictionary


for k in gen_random_color():
    print(k)
