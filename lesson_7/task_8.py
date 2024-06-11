def number_check(data):
    c = bool

    for k in data:
        if k > 0:
            c = True
            continue
        elif k < 0:
            c = False
            break
        if c == True:
            continue
    print(c)

a = [1,2,5,9]
number_check(a)