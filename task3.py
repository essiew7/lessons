class Fridge:
    def __init__(self, brand, capacity, model):
        self.brand = brand
        self.model = model
        self.capacity = capacity

    def open_door(self):
        return "Door open"

    def close_door(self):
        return "Door closed"

    def turn_on(self):
        return "ON"

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Capacity: {self.capacity}"


fridge_1 = Fridge("Atlant", "300 Liters", "Ultra Mega Fridge")
print(fridge_1, fridge_1.open_door())
