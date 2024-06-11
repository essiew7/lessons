def starts_a(data):
    data = [k for k in data if k.startswith("a") or k.startswith("A")]
    print(data)

a = ['anton','Anton','pomidor','john','bob']
starts_a(a)