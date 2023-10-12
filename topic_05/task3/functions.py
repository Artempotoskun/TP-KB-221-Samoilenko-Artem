def dodavannia(a, b):
    return a + b

def vidnimannia(a, b):
    return a - b

def mnozhennia(a, b):
    return a * b

def dilennia(a, b):
    if b == 0:
        raise ZeroDivisionError("Помилка: ділення на нуль")
    return a / b
