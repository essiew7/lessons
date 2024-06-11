word = input("Введите букву английского алфавита : ").lower()

match (word):
    case "monday" | "mon" | "mo":
        print("Будний день")
    case "tuesday" | "tue" | "tu":
        print("Будний день")
    case "wednesday" | "wed" | "we":
        print("Будний день")
    case "thursday" | "thu" | "th":
        print("Будний день")
    case "friday" | "fri" | "fr":
        print("Будний день")
    case "saturday" | "sat" | "sa":
        print("Выходной")
    case "sunday" | "sun" | "sn":
        print("Выходной")
