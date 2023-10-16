list= [
    {"name": "Bob", "phone": "0631234567", "age": 20, "email": "bob@example.com"},
    {"name": "Emma", "phone": "0631234567", "age": 22, "email": "emma@example.com"},
    {"name": "Jon", "phone": "0631234567", "age": 21, "email": "jon@example.com"},
    {"name": "Zak", "phone": "0631234567", "age": 19, "email": "zak@example.com"}
]

def printAllList():
    for student in list:
        strForPrint = f"Student name is {student['name']}, Age is {student['age']}, Phone is {student['phone']}, Email is {student['email']}"
        print(strForPrint)

def addNewElement():
    name = input("Please enter student name: ")
    age = int(input("Please enter student age: "))
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    new_student = {"name": name, "phone": phone, "age": age, "email": email}
    
    insertPosition = 0
    for i, student in enumerate(list):
        if name > student["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, new_student)
    
    print("New element has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for student in list:
        if name == student["name"]:
            deletePosition = list.index(student)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print("Element has been deleted")

def updateElement():
    name = input("Please enter name to be updated: ")
    for student in list:
        if name == student["name"]:
            new_name = input("Please enter the new name: ")
            new_age = int(input("Please enter the new age: "))
            new_phone = input("Please enter the new phone: ")
            new_email = input("Please enter the new email: ")
            student["name"] = new_name
            student["age"] = new_age
            student["phone"] = new_phone
            student["email"] = new_email
            print("Student information updated")
            break
    else:
        print("Student not found")

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        if choice.upper() == "C":
            print("New element will be created:")
            addNewElement()
        elif choice.upper() == "U":
            print("Existing element will be updated")
            updateElement()
        elif choice.upper() == "D":
            print("Element will be deleted")
            deleteElement()
        elif choice.upper() == "P":
            print("List will be printed")
            printAllList()
        elif choice.upper() == "X":
            print("Exit")
            break
        else:
            print("Wrong choice")

main()
