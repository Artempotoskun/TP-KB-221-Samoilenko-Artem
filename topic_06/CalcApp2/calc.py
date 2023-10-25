import functions
import operations
import logging

logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    while True:
        operator = operations.get_operator()

        if operator.lower() == 'q':
            break

        operand1 = operations.get_operand()
        operand2 = operations.get_operand()

        result = None
        error_message = None

        try:
            match operator:
                case '+':
                    result = functions.dodavannia(operand1, operand2)
                case '-':
                    result = functions.vidnimannia(operand1, operand2)
                case '*':
                    result = functions.mnozhennia(operand1, operand2)
                case '/':
                    result = functions.dilennia(operand1, operand2)
                case '_':
                    error_message = "Неправильна операція! Спробуйте ще раз."
        except Exception as e:
            error_message = str(e)

        if result is not None:
            logging.info(f"{operand1} {operator} {operand2} = {result}")
            print(f"Operation result {result}")
        else:
            logging.error(f"Error: {error_message}")
            print(error_message)

main()
