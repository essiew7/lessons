def fibo_nums():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

cycle = ''
while cycle.lower() != 'end':
    for k in fibo_nums():
        print(k)
        cycle = input('для остановки цикла введите "end".')
        if cycle.lower() == 'end':
            break
