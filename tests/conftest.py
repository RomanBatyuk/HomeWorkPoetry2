import pytest


@pytest.fixture
def data_for_verification_processing():
    """Данные для функции filter_by_state"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def data_for_verification_processing_2():
    """Результат функции filter_by_state в тесте test_filter_by_state"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def data_for_verification_processing_3():
    """Результат функции filter_by_state в тесте test_filter_by_state_incorrect_input_data"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def data_for_verification_processing_4():
    """Результат функции sort_by_date в тетсте test_sort_by_date при rev: bool = False"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def data_for_verification_processing_5():
    """Результат функции sort_by_date в тетсте test_sort_by_date при rev: bool = True"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def data_for_verification_processing_6():
    """Данные для функции sort_by_date"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:36:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:37:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:34:29.512364"},
    ]


@pytest.fixture
def data_for_verification_processing_7():
    """Результат функции sort_by_date в тесте test_sort_by_date при rev: bool = False"""
    return [
        {"date": "2019-07-03T18:34:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2019-07-03T18:36:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2019-07-03T18:37:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


@pytest.fixture
def data_for_verification_processing_8():
    """Результат функции sort_by_date в тесте test_sort_by_date при rev: bool = True"""
    return [
        {"date": "2019-07-03T18:37:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2019-07-03T18:36:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2019-07-03T18:34:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


@pytest.fixture
def data_transaction_descriptions():
    """Тестовые данные для функции transaction_descriptions"""
    return []


@pytest.fixture
def data_transaction_descriptions_2():
    """Ожидаемый результат теста функции transaction_descriptions"""
    return ["Ошибка! Список транзакций отстутствует"]


@pytest.fixture
def data_transaction_descriptions_3():
    """Тестовые данные для функции transaction_descriptions"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def data_transaction_descriptions_4():
    """Ожидаемый результат теста функции transaction_descriptions"""
    return ["Перевод организации", "Перевод со счета на счет"]


@pytest.fixture
def data_card_number_generator():
    """Ожидаемый результат теста функции card_number_generator"""
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


@pytest.fixture
def data_card_number_generator_2():
    """Ожидаемый результат теста функции card_number_generator"""
    return [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
