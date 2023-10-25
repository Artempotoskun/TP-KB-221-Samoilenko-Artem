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

