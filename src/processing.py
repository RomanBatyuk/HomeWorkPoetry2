from datetime import datetime


def filter_by_state(list_inp: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари
    у которых ключ state соответствует указанному значению"""
    new_list = [i for i in list_inp if i["state"] == state]
    if not new_list:
        raise Exception("Словарь с указанным статусом state отсутствует")
    return new_list


def sort_by_date(list_inp: list[dict], rev: bool = False) -> list[dict]:
    """Функция должна возвращать новый список, отсортированный по дате"""
    for i in list_inp:
        try:
            datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            raise ValueError("Ввод данных должен осуществляться в формате: '2019-07-03T18:36:29.512364'")

        else:
            return sorted(list_inp, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=rev)
