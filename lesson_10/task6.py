def bigger_than_ten(num_list):
    new_list = list(filter(lambda x: (x > 10),num_list))
    return new_list


a = [k for k in range(1,25)]
print(bigger_than_ten(a))


