import logging
from functions import CalculatorFunctions
from operations import CalculatorOperations

logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Calculator:
    def __init__(self):
        self.operations = CalculatorOperations()
        self.functions = CalculatorFunctions()

    def run(self):
        while True:
            operator = self.operations.get_operator()

            if operator.lower() == 'q':
                break

            operand1 = self.operations.get_operand()
            operand2 = self.operations.get_operand()

            result = None
            error_message = None

            try:
                match operator:
                    case '+':
                        result = self.functions.dodavannia(operand1, operand2)
                    case '-':
                        result = self.functions.vidnimannia(operand1, operand2)
                    case '*':
                        result = self.functions.mnozhennia(operand1, operand2)
                    case '/':
                        result = self.functions.dilennia(operand1, operand2)
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

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
