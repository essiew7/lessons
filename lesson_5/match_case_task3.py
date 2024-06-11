fruit = input("Введите название фрукта : ").lower()
dictionary = {'apple': "red", 'banana': "yellow", "orange": "orange",
              "grape": "green", "plum": "purple", "blueberry": "blue"}

match fruit:
    case "apple":
        print(dictionary[fruit])
    case "banana":
        print(dictionary[fruit])
    case "orange":
        print(dictionary[fruit])
    case "grape":
        print(dictionary[fruit])
    case "plum":
        print(dictionary[fruit])
    case "blueberry":
        print(dictionary[fruit])
