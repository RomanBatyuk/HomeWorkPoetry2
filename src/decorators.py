from functools import wraps


def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции
    а также ее результаты или возникшие ошибки"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok. {result}\n")
                else:
                    print(f"{func.__name__} ok. Inputs: {result}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs:  {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs:  {args}, {kwargs}")
                raise

        return inner

    return wrapper


@log(filename="../mylog.txt")
def div(x, y):
    """Функция деления"""
    return x / y


# div(2, 1)


@log(filename="../mylog.txt")
def div_1(x, y):
    """Функция деления"""
    return x / y


@log(filename="../mylog.txt")
def amount(x, y):
    """Функция сложения"""
    return x + y


# amount(2, 4)


@log(filename="../mylog.txt")
def subtraction(x, y):
    """Функция вычитания"""
    return x - y


# subtraction(4, 2)


@log(filename="../mylog.txt")
def subtraction_1(x, y):
    """Функция вычитания"""
    return x - y


# subtraction_1(0, 2)
