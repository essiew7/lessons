def similarity(list1,list2):
    list3 = [list1 for list1 in list2 if list1 in list2]
    print(list3)

a = [k for k in range(1,11)]
b = [k for k in range(1,11,2)]
similarity(a,b)
