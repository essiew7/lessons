def sort(a):
    a = [{"name": "Edward", "age": 17, "marks": [1, 2, 7, 4, 5]},
        {"name": "Bob", "age": 21, "marks": [1, 5, 3, 7, 5]},
        {"name": "Tom", "age": 32, "marks": [1, 3, 8, 4, 9]}]
    i=1
    c = 0

    for person in a:
        if person["age"] < a[i]["age"]:
            c = a[i]["age"]
            a[i]["age"] = person["age"]
            person["age"] = c
            i = +1
    print(a)

# b = [{"name": "Edward", "age": 17, "marks": [1, 2, 7, 4, 5]},
#   {"name": "Bob", "age": 32, "marks": [1, 5, 3, 7, 5]},
#   {"name": "Tom", "age": 21, "marks": [1, 3, 8, 4, 9]}]
# sort(b)


