import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(data_for_verification_processing, data_for_verification_processing_2):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(data_for_verification_processing) == data_for_verification_processing_2


def test_filter_by_state_incorrect_input_data(data_for_verification_processing_3):
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    with pytest.raises(Exception, match="Словарь с указанным статусом state отсутствует"):
        filter_by_state(data_for_verification_processing_3)


@pytest.mark.parametrize(
    "list_inp, state, list_result",
    [
        ("data_for_verification_processing", "EXECUTED", "data_for_verification_processing_2"),
        ("data_for_verification_processing", "CANCELED", "data_for_verification_processing_3"),
    ],
)
def test_filter_by_state_with_different_status_values_state(request, list_inp, state, list_result):
    """Тест функции с параметризацией значений статуса state"""
    list_inp = request.getfixturevalue(list_inp)
    list_result = request.getfixturevalue(list_result) if isinstance(list_result, str) else list_result
    assert filter_by_state(list_inp, state) == list_result


@pytest.mark.parametrize(
    "list_inp, rev, sort_list",
    [
        ("data_for_verification_processing", False, "data_for_verification_processing_4"),
        ("data_for_verification_processing", True, "data_for_verification_processing_5"),
        ("data_for_verification_processing_6", False, "data_for_verification_processing_7"),
        ("data_for_verification_processing_6", True, "data_for_verification_processing_8"),
    ],
)
def test_sort_by_date(request, list_inp, rev, sort_list):
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания"""
    list_inp = request.getfixturevalue(list_inp)
    sort_list = request.getfixturevalue(sort_list)
    assert sort_by_date(list_inp, rev) == sort_list


def test_sort_by_date_not_correct_formats():
    """Тестирование работs функции с некорректными или нестандартными форматами дат"""
    with pytest.raises(ValueError):
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-03T18_29.512364"}])
