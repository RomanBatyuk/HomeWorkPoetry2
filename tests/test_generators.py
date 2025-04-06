import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


@pytest.mark.parametrize("currency, expected_count", [("USD", 3), ("RUB", 2)])
def test_filter_by_currency(currency, expected_count):
    """Тест проверяющий, что функция корректно фильтрует транзакции по заданной валюте"""
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == currency


def test_filter_by_currency_empty_list():
    """Проверка правильности работы функции, когда транзакции в заданной валюте отсутствуют"""
    result = list(filter_by_currency([], "USD"))
    assert result == ["Ошибка! Список транзакций отстутствует"]


def test_filter_by_currency_no_transactions():
    """Тест проверяющий что генератор не завершается ошибкой при обработке пустого списка
    или списка без соответствующих валютных операций"""
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == ["Ошибка! Транзакции в заданной валюте отсутствуют"]


def test_transaction_descriptions():
    """Тест проверяющий, что функция возвращает корректные описания для каждой транзакции"""
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize(
    "waiting, result",
    [
        ("data_transaction_descriptions", "data_transaction_descriptions_2"),
        ("data_transaction_descriptions_3", "data_transaction_descriptions_4"),
    ],
)
def test_transaction_descriptions_2(waiting, result, request):
    waiting_data = request.getfixturevalue(waiting)
    result_data = request.getfixturevalue(result)
    assert list(transaction_descriptions(waiting_data)) == result_data


@pytest.mark.parametrize(
    "start, end, result",
    [(1, 5, "data_card_number_generator"), (9999999999999995, 9999999999999999, "data_card_number_generator_2")],
)
def test_card_number_generator(start, end, result, request):
    """Проверка функции на правильность выдаваемых номеров карт в заданном диапазоне"""
    expected = request.getfixturevalue(result)
    waiting_data = list(card_number_generator(start, end))
    assert waiting_data == expected


def test_card_number_generator_2(data_card_number_generator):
    """Проверка корректности форматирования номеров карт"""
    generator_2 = list(card_number_generator(1, 5))
    assert generator_2 == data_card_number_generator


@pytest.mark.parametrize(
    "start, end, expected",
    [(1, 1, ["0000 0000 0000 0001"]), (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"])],
)
def test_card_number_generator_boundaries(start, end, expected):
    """Проверка функции, на корректную обработку крайних значений диапазона и правильность завершения генерации"""
    result = list(card_number_generator(start, end))
    assert result == expected
