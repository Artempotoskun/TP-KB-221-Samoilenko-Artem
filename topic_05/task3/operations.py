def get_operand():
    try:
        operand = float(input("Введіть число: "))
        return operand
    except ValueError:
        print("Помилка: введіть коректне число.")
        return get_operand()

def get_operator():
    operator = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")
    return operator

def perform_operation(operator, operand1, operand2, functions):
    if operator == '+':
        return functions.dodavannia(operand1, operand2)
    elif operator == '-':
        return functions.vidnimannia(operand1, operand2)
    elif operator == '*':
        return functions.mnozhennia(operand1, operand2)
    elif operator == '/':
        return functions.dilennia(operand1, operand2)
    else:
        print("Неправильна операція! Спробуйте ще раз.")
        return None
