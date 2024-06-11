def nums3(num_list):
    new_list = list(filter(lambda x: (x % 3 == 0),num_list))
    return new_list


a = [k for k in range(1,25)]
print(nums3(a))
