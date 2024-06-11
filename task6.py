class Student:
    def __init__(self, name, surname, age, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.marks = marks

    def avg_mark(self):
        return f"Средний балл составил : {round(sum(self.marks) / len(self.marks), 3)}"

    def get_achievements(self):
        return f"{self.name} {self.surname} убил море. Отныне его называют мертвым морем."

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Marks: {self.marks}"


student_01 = Student("Chuck", "Norris", 84, [10, 7, 6, 12, 9, 9, 8])
print(student_01)
print(student_01.get_achievements())
print(student_01.avg_mark())
