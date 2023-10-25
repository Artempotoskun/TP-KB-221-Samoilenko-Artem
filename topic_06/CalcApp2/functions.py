def dodavannia(a, b):
    return a + b

def vidnimannia(a, b):
    return a - b

def mnozhennia(a, b):
    return a * b


def dilennia(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("ERROR: ZeroDivisionError!!!")
        return None