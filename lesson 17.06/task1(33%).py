class Vehicle:
    def __init__(self, name, engine, height, weight, width, length, key_lock=None):
        self.name = name
        self.engine = engine
        self.height = height
        self.weight = weight
        self.width = width
        self.length = length
        self.key_lock = key_lock

    def lock(self):
        self.key_lock = "Закрыт"
        return "Транспортное средство закрыто."

    def unlock(self):
        self.key_lock = "Открыт"
        return "Транспортное средство открыто."

    def __str__(self):
        return (f"{self.name}, Замок - {self.key_lock}, Масса - {self.weight}, Двигатель - {self.engine}, Параметры: L - {self.length} "
                f"H - {self.height}, B - {self.width}")

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


test = Vehicle("Самолет", "petrol", 5, 3200, 6, 10)
test1 = Vehicle("Самолет", "petrol", 5, 3220, 6, 10)



class Car(Vehicle):

    def __init__(self, name, engine, height, weight, width, length, key_lock=None,):
        super(Car, self).__init__(name, engine, height, weight, width, length, key_lock)
        







