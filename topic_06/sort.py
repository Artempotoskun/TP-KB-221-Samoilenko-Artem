students = [
    {"name": "Alice", "mark": 90},
    {"name": "Bob", "mark": 85},
    {'name': 'Peter', 'mark': 65},
    {'name': 'Evgeniy', 'mark': 88},
    {'name': 'Valeriy', 'mark': 67},
    {'name': 'Kyrylo', 'mark': 74},
    {'name': 'Viktoria', 'mark': 55},
    {'name': 'Alexander', 'mark': 83},
    {"name": "Kate", "mark": 88},
    {"name": "David", "mark": 92}
]

sorted_students_by_name = sorted(students, key=lambda x: x.get("name", ""))
sorted_students_by_mark = sorted(students, key=lambda x: x.get("mark", 0))

print("Сортування за іменем:")
for student in sorted_students_by_name:
    print(student)

print("\nСортування за оцінкою:")
for student in sorted_students_by_mark:
    print(student)
