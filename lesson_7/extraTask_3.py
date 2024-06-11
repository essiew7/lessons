def operation_range(start, end, step, operator):
    k = [n for n in range(start,end+1,step)]
    if operator == "+":
        print(sum(k))
    elif operator == "-":
        b = 0
        c = [k[j] - k[j + 1] for j in range(len(k) - 1)]
        for k in c:
            b -= -k
        print(b)

operation_range(1,10,3,"-")
