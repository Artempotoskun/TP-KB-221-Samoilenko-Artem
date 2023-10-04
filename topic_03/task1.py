def dodavannia(a, b):
    return a + b

def vidnimannia(a, b):
    return a - b

def mnozhennia(a, b):
    return a * b

def dilennia(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль"

while True:
    try:
        operand1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")

        if operator.lower() == 'q':
            break

        operand2 = float(input("Введіть друге число: "))

        if operator == '+':
            print("Результат: ", dodavannia(operand1, operand2))
        elif operator == '-':
            print("Результат: ", vidnimannia(operand1, operand2))
        elif operator == '*':
            print("Результат: ", mnozhennia(operand1, operand2))
        elif operator == '/':
            print("Результат: ", dilennia(operand1, operand2))
        else:
            print("Неправильна операція! Спробуйте ще раз.")

    except ValueError:
        print("Помилка: введіть коректне число.")
    except Exception as e:
        print("Помилка: ", e)
