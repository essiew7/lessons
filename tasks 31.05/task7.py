def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n**0.5) + 1
    for d in range(3, max_div, 2):
        if n % d == 0:
            return False
    return True

def gen_simple_nums(num):
    yield 2
    for k in range(3,num +1, 2):
        if is_prime(k):
            yield k

for k in gen_simple_nums(50):
    print(k)
