from src.masks import get_mask_card_number, get_mask_account


import pytest


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_not_the_format():
    """Ошибка о не том формате номера карты"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("700079228960636")

    assert str(exc_info.value) == "Номер должен содержать 16 цифр"


def test_get_mask_card_number_not_the_format_2():
    """Ошибка о не том формате номера карты"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")

    assert str(exc_info.value) == "Номер должен содержать 16 цифр"


def test_mask_account_proper_disguise():
    """Тестирование правильности маскирования номера счета"""
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize("mask_account, mask_card", [
    ("64686473678894779589", "**9589"),
    ("35383033474447895560", "**5560"),
    ("73654108430135874305", "**4305")
])

def test_get_mask_account_different_account_formats(mask_account, mask_card):
    """Проверка работы функции с различными счетами"""
    assert get_mask_account(mask_account) == mask_card

def test_get_mask_account_not_the_format():
    """Ошибка о не том формате номера счета"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("7365410843013587430")
    assert str(exc_info.value) == "Номер должен содержать 20 цифр"