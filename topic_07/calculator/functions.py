class CalculatorFunctions:
    @staticmethod
    def dodavannia(a, b):
        return a + b

    @staticmethod
    def vidnimannia(a, b):
        return a - b

    @staticmethod
    def mnozhennia(a, b):
        return a * b

    @staticmethod
    def dilennia(a, b):
        if b == 0:
            raise ZeroDivisionError("Помилка: ділення на нуль")
        return a / b
