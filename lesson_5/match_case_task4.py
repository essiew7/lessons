mark = int(input("Введите оценку : "))
if mark < 0 or mark > 5: print("Введите оценку в диапазоне от 1 до 5!"), exit()

match mark:
    case 1:
        print("very bad")
    case 2:
        print("bad")
    case 3:
        print("its ok")
    case 4:
        print("good")
    case 5:
        print("very good")
    case _:
        print("None")