dictionary = {}
dictionary["строка"] = 12
dictionary[("Jason", "Statham")] = [1,"2",[1,"2","pomidor"]]
print(dictionary)
print(dictionary["строка"])
del dictionary["строка"]
print(dictionary.keys())