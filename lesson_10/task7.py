def upper_check(arrays):
    new_list = list(filter(lambda x: (x.isupper()), arrays))
    return new_list


a = ["монитор", "МЫШЬ","клавиатура","НаушНики"]
print(upper_check(a))


