from random import choice, randint


class User:
    def __init__(self, name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    def __str__(self):
        return (f"{self.name}, {self.surname}, Age - {self.age}, Country - {self.country}, Gender - {self.gender},"
                f" prof - {self.profession}")


    def email(self):
        return f"Ваш e-mail -> {self.name.lower()}{self.surname.lower()}{2024 - self.age}@gmail.com"

    def date_of_birth(self):
        birth = 2024 - self.age
        return f"Вы родились в {birth} году!"

    @staticmethod
    def create_doc():
        db_names = ["Tom", "Bob", "John", "Sam", "Jason", "Cristiano", "Lionel"]
        db_surnames = ["Stone", "Ronaldo", "Messi", "Statham", "Neuer", "Bale", "Marcelo"]
        db_countries = ["Belgium", "Spain", "USA", "Portugal", "England", "Germany", "Argentina"]
        doctor = User(choice(db_names), choice(db_surnames), randint(24, 64), choice(db_countries), "Male", "Doctor")
        return doctor

    @staticmethod
    def create_police():
        db_names = ["Tom", "Bob", "John", "Sam", "Jason", "Cristiano", "Lionel"]
        db_surnames = ["Stone", "Ronaldo", "Messi", "Statham", "Neuer", "Bale", "Marcelo"]
        db_countries = ["Belgium", "Spain", "USA", "Portugal", "England", "Germany", "Argentina"]
        policeman = User(choice(db_names), choice(db_surnames), randint(24, 64), choice(db_countries), "Helicopter", "Policeman")
        return policeman

    @staticmethod
    def create_teacher():
        db_names = ["Alice", "Nora", "Jess", "Sofia", "Polina", "Kate", "Anna"]
        db_surnames = ["Stone", "Ronaldo", "Messi", "Statham", "Neuer", "Bale", "Marcelo"]
        db_countries = ["Belgium", "Spain", "USA", "Portugal", "England", "Germany", "Argentina"]
        teacher = User(choice(db_names), choice(db_surnames), randint(24, 64), choice(db_countries), "Female",
                         "Teacher")
        return teacher


test = User.create_teacher()
print(test)
print(test.date_of_birth())
print(test.email())
print(User.create_doc())
print(User.create_police())
print(User.create_teacher())


