def letter_e_check(data):
    letter_e = "eEеЕ"
    res = []
    for k in data:
        for c in k:
            if c in letter_e:
                res.append(k)

    print(res)

a = ['epkjoghfrd', 'asd', 'iotgfi', 'Ekgfgf']
letter_e_check(a)
