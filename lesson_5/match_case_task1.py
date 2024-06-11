letter = input("Введите букву английского алфавита : ").lower()

match (letter):
    case "e" | "y" | "u" | "i" | "o" | "a" :
        print("Гласная буква")
    case "q"|"w"|"r"|"t"|"p"|"s"|"d"|"f"|"g"|"h"|"j"|"k"|"l"|"z"|"x"|"c"|"v"|"b"|"n"|"m" :
        print("Согласная буква")
    case _:
        print("None")
