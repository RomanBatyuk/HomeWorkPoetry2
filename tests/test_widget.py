from src.widget import mask_account_card, get_date


import pytest

@pytest.mark.parametrize("card_or_account, result",
    [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ])

def test_mask_account_card_correctness_of_work(card_or_account, result):
    '''Проверка работоспособности функции при разных входных данных'''
    assert mask_account_card(card_or_account) == result

def test_mask_account_card_incorrect_input_data():
    '''Проверка работы функции с некорректными данными'''
    with pytest.raises(ValueError):
        mask_account_card("Счет 7365410843013587430")

    with pytest.raises(ValueError):
        mask_account_card("Maestro 15968378687051999")

    with pytest.raises(ValueError):
        mask_account_card("Visa Classic 68319824767376")


def test_get_date():
    '''Тестирование правильности преобразования даты'''
    assert get_date("2024-03-11") == "2024-03-11"


def test_get_date_incorrect_input():
    '''Проверка работы функции с некорректными данными'''
    with pytest.raises(ValueError):
        get_date("2024-13-11T02:26:18.671407")

    with pytest.raises(ValueError):
        get_date("2024-03-11T")

    with pytest.raises(ValueError):
        get_date("24-03-11T02:26:18.671407")

    with pytest.raises(ValueError):
        get_date("")