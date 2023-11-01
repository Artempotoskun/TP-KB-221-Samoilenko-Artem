# init
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name)  # Виведе "Alice"
print(person1.age)   # Виведе 25


# str

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

person1 = Person("Alice", 25)
print(str(person1))  # Виведе "Person: Alice, Age: 25"


# call

class Calculator:
    def __call__(self, a, b):
        return a + b

add = Calculator()
result = add(5, 3)
print(result)  # Виведе 8
