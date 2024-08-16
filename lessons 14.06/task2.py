class Restaurant:
    def __init__(self, menu=None, order_items=None):
        self.menu = list(menu) if menu else []
        self.order_items = list(order_items) if order_items else []

    def __str__(self):
        print("МЕНЮ")
        return str(self.menu)

    def add_dish_to_menu(self, dish):
        self.menu.append(dish.lower())

    def remove_dish_from_menu(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"Блюдо '{dish}' удалено из меню.")
        else:
            print(f"Блюда '{dish}' нет в меню.")

    def order(self):
        for k in range(3):print("\033[H\033[J")
        print("Блюда для заказа.")
        print(self.menu)
        k = input("Введите название блюда, которое хотите заказать: ")
        if k.lower() in self.menu:
            print("Блюдо заказано!")
            self.order_items.append(k)
        else:
            print("Такого блюда нет в меню!")

    def ordered_items(self):
        print(f'Заказанные блюда: {self.order_items}')


rest_test = Restaurant()
rest_test.add_dish_to_menu("Каша")
rest_test.add_dish_to_menu("рыба")
print(rest_test)
rest_test.remove_dish_from_menu("рыба")
print(rest_test)
rest_test.order()
rest_test.ordered_items()