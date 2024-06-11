def beetween_5_and_10(num_list):
    new_list = list(filter(lambda x: (x in range(5,11)),num_list))
    return new_list


a = [k for k in range(1,25)]
print(beetween_5_and_10(a))
