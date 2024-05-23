students = {"name": "Elon", "age": "77", "marks": [7, 4, 5, 8, 9, 3, 1, 10]}
students2 = {"name": "Viktor", "age": "23", "marks": [2, 3, 1, 7, 2, 4, 5, 4]}
average = 0
average = sum(students["marks"])/ (len("marks") + 1)

if average < 7: del students
print(students["name"],"Средний балл - ",average)
print(students2)
average = sum(students2["marks"])/ (len("marks") + 1)
if average < 7: students2 = {}
print(students2)
