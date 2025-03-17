from datetime import datetime


def filter_by_state(list_inp: list[dict], state: str='EXECUTED') -> list[dict]:
    '''Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению'''
    new_list = []
    for i in list_inp:
        if i['state'] == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_inp: list[dict], rev: bool=False) -> list[dict]:
    '''Функция должна возвращать новый список, отсортированный по дате'''
    return sorted(list_inp, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=rev)
