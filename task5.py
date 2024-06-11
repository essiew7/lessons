class House:
    def __init__(self, floors, rooms, square):
        self.floors = floors
        self.rooms = rooms
        self.square = square

    def house_price(self):
        return  f"Price = {self.floors * self.rooms * self.square * 20}$"

    def __str__(self):
        return f"Floors: {self.floors}, Rooms: {self.rooms}, Square: {self.square} m²"


house1 = House(2, 5, 89)
print(house1)
print(house1.house_price())
