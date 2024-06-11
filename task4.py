class Human:
    def __init__(self, name, surname, age, number):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number

    def sit(self):
        return f"{self.name} сел."

    def up(self):
        return f"{self.name} встал."

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Number: {self.number}"


Human_1 = Human("Senior", "Pomidor", "55", "+375441234567")
print(Human_1)
print(Human_1.sit())
