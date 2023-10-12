import functions
import operations

while True:
    operand1 = operations.get_operand()
    operator = operations.get_operator()

    if operator.lower() == 'q':
        break

    operand2 = operations.get_operand()

    result = operations.perform_operation(operator, operand1, operand2, functions)
    if result is not None:
        print("Результат:", result)
