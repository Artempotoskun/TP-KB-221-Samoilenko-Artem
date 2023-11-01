class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Charlie", 23),
     Student("Bob", 21),
    Student("Alice", 22),

]

sorted_students = sorted(students, key=lambda student: student.name)

for student in sorted_students:
    print(f"Name: {student.name}, Age: {student.age}")