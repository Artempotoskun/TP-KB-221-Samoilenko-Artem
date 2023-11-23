from sys import argv
import csv

if len(argv) == 1:
    back_file = 'lab2.csv'
else:
    back_file = argv[1]

def LoadBackFile(back_file):
    data = []
    with open(back_file) as file:
        reader = csv.DictReader(file)

        for row in reader:
            lowercased_row = {key.lower(): value for key, value in row.items()}
            data.append(lowercased_row)
    params = tuple(data[0].keys()) 
    if len(data) == 0:
        params = ('name', 'phone')

    return data, params


def GetNewParams(param_tuple) -> tuple:
    new_params = {}
    for param in param_tuple:
        new_params[param] = input(f'Please enter student {param}: ')
    return new_params


def printAllList(param_tuple, students_list):
    print("#" * 10 + '  All list  ' + '#' * 10)
    for elem in students_list:
        print('Student : ', end='')
        for param in param_tuple:
            str_for_print = f"{param} is " + f"{elem[param]}"
            print(str_for_print, end=', ')
        print('\n')
    print("#" * 20)
    return



def addNewElement(students_list, param_tuple):
    new_item = GetNewParams(param_tuple)
    print(new_item['name'])
    insert_position = 0
    for item in students_list:
        if new_item['name'] > item["name"]:
            insert_position += 1
        else:
            break
    students_list.insert(insert_position, new_item)
    print("New element has been added")
    return



def deleteElement(students_list):
    name = input("Please enter name to be deleted: ")
    delete_position = -1
    for item in students_list:
        if name == item["name"]:
            delete_position = students_list.index(item)
            break
    if delete_position == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(delete_position))
        del students_list[delete_position]
    return



def updateElement(students_list, param_tuple):
    name = input("Please enter name to be updated: ")
    update_position = -1
    for item in students_list:
        if name == item["name"]:
            update_position = students_list.index(item)
            break

    if update_position == -1:
        print("Element was not found")
    else:
        print("Update position " + str(update_position))
        print('Enter new params:')
        new_params = GetNewParams(param_tuple)
        if new_params['name'] == students_list[update_position]['name']:
            students_list[update_position] = new_params
        else:
            del students_list[update_position]
            insert_position = 0
            for item in students_list:
                if new_params['name'] > item["name"]:
                    insert_position += 1
                else:
                    break
            students_list.insert(insert_position, new_params)

        print('List was updated!')



def main(students_list, param_tuple):
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "C" | "c":
                print("New element will be created:")
                addNewElement(students_list, param_tuple)
                printAllList(param_tuple=param_tuple, students_list=students_list)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(students_list=students_list, param_tuple=param_tuple)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(students_list)
            case "P" | "p":
                print("List will be printed")
                printAllList(param_tuple=param_tuple, students_list=students_list)
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")


def SaveAllData(students_list, params, path):
    with open(path, "w", newline='') as csvfile:
        fieldnames = params
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in students_list:
            writer.writerow(i)
    print('All data saved!')


if __name__ == '__main__':
    list, params = LoadBackFile(back_file)
    main(list, params)
    SaveAllData(list, params, "lab2_out.csv")
