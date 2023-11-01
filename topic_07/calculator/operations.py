class CalculatorOperations:
    @staticmethod
    def get_operand():
        while True:
            try:
                operand = float(input("Введіть число: "))
                return operand
            except ValueError:
                print("Помилка: введіть коректне число.")

    @staticmethod
    def get_operator():
        operator = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")
        return operator
