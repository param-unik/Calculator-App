def do_addition(a: int, b: int):
    return a + b


def do_subtract(a: int, b: int):
    return a - b


def do_multiply(a: int, b: int):
    return a * b


def do_division(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Division by zero error, Hence the operation is not possible!")
