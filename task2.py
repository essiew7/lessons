class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def engine_on(self):
        return "Двигатель запущен"

    def engine_off(self):
        return "Двигатель остановлен"


car_test = Car("Daewoo", "Matiz", 2010, "red")
print(car_test.brand,car_test.model)
print(car_test.engine_on())
