import pytest

from src.decorators import log


def test_log():
    """Тестирование декоратора log"""

    @log(filename="mylog.txt")
    def div(x, y):
        """Тестирование деления"""
        return x / y

    result_div = div(2, 1)
    assert result_div == 2

    @log(filename="mylog.txt")
    def div_1(x, y):
        """Тестирование деления"""
        return x / y

    with pytest.raises(ZeroDivisionError):
        div_1(2, 0)

    @log(filename="mylog.txt")
    def amount(x, y):
        """Тестирование сложения"""
        return x + y

    result_amount = amount(2, 4)
    assert result_amount == 6

    @log(filename="mylog.txt")
    def subtraction(x, y):
        """Тестирование вычитания"""
        return x - y

    result_subtraction = subtraction(4, 2)
    assert result_subtraction == 2

    @log(filename="mylog.txt")
    def subtraction_1(x, y):
        """Тестирование вычитания"""
        return x - y

    result_subtraction = subtraction_1(0, 2)
    assert result_subtraction == -2


def test_log_1(capsys):
    """Тестирование деления, с использованием фикстуры capsys"""

    @log()
    def div_1(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div_1(2, 0)

    captured = capsys.readouterr()
    assert captured.out == "div_1 error: division by zero. Inputs:  (2, 0), {}\n"
