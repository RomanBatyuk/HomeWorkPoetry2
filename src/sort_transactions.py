import csv
import json
import re
from collections import Counter

import pandas as pd
from mypy.messages import capitalize

list_transact = "data/data.json"
list_transact_2 = "transactions/transactions.csv"
list_transact_3 = "transactions/transactions_excel.xlsx"


def search_operation_json(list_transact: list[dict], search_element: str):
    """Функция для json файла, принимает путь к файлу и строку для поиска,
    возвращает список словарей с операциями, у которых в описании есть строка, переданная аргументу функции"""
    print("Для обработки выбран JSON-файл")
    while search_element not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции '{search_element}' недоступен")
        search_element = str(
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
        ).upper()

    with open(list_transact, "r", encoding="utf-8") as f:
        data_1 = json.load(f)
        filtered_transact = [i for i in data_1 if re.search(search_element, i["state"])]
        print(f"Операции отфильтрованы по статусу '{search_element}'")
        if not filtered_transact:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            return []

        sort_date = capitalize(input("Отсортировать операции по дате? Да/Нет\n"))
        if sort_date == "Да":
            sort_rev_true_false = capitalize(input("Отсортировать 'по возрастанию' или 'по убыванию'?\n"))
            reverse_sort = True if sort_rev_true_false == "по убыванию" else False

            sorted_list = sorted(filtered_transact, key=lambda x: x["date"], reverse=reverse_sort)

            conclusion_rub_transact = capitalize(input("Выводить только рублевые транзакции? Да/Нет\n"))
            if conclusion_rub_transact == "Да":
                result_list = [t for t in sorted_list if t["operationAmount"]["currency"]["code"] == "RUB"]
            else:
                result_list = sorted_list

            if not result_list:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                return []

            print("Распечатываю итоговый список транзакций...")
            return result_list
        else:
            sort_rev_true_false = capitalize(input("Отсортировать 'по возрастанию' или 'по убыванию'?\n"))
            reverse_sort = True if sort_rev_true_false == "по убыванию" else False

            sorted_list = sorted(filtered_transact, key=lambda x: x["date"], reverse=reverse_sort)

            conclusion_rub_transact = capitalize(input("Выводить только рублевые транзакции? Да/Нет\n"))
            if conclusion_rub_transact == "Да":
                result_list = [t for t in sorted_list if t["operationAmount"]["currency"]["code"] == "RUB"]
            else:
                result_list = sorted_list

            if not result_list:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                return []

            print("Распечатываю итоговый список транзакций...")
            return result_list


def search_operation_csv(list_transact_2: list[dict], search_element: str):
    """Функция для csv файла, принимает два аргумента: список с транзакциями и строку для поиска,
    возвращает список словарей с операциями, у которых в описании есть строка, переданная аргументу функции"""
    print("Для обработки выбран CSV-файл")
    while search_element not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции '{search_element}' недоступен")
        search_element = str(
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
        ).upper()

    transactions = []
    with open(list_transact_2, "r", encoding="utf-8") as file:
        df = csv.DictReader(file, delimiter=";")
        for row in df:
            transactions.append(
                {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "amount": row["amount"],
                    "currency_name": row["currency_name"],
                    "currency_code": row["currency_code"],
                    "from": row["from"],
                    "to": row["to"],
                }
            )

    filtered_transact = [i for i in transactions if re.search(search_element, i["state"])]
    print(f"Операции отфильтрованы по статусу '{search_element}'")
    if not filtered_transact:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return []

    sort_date = capitalize(input("Отсортировать операции по дате? Да/Нет\n"))
    if sort_date == "Да":
        sort_rev_true_false = capitalize(input("Отсортировать 'по возрастанию' или 'по убыванию'?\n"))
        reverse_sort = True if sort_rev_true_false == "по убыванию" else False

        sorted_list = sorted(filtered_transact, key=lambda x: x["date"], reverse=reverse_sort)

        conclusion_rub_transact = capitalize(input("Выводить только рублевые транзакции? Да/Нет\n"))
        if conclusion_rub_transact == "Да":
            result_list = [t for t in sorted_list if t["currency_code"] == "RUB"]
        else:
            result_list = sorted_list

        if not result_list:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            return []

        print("Распечатываю итоговый список транзакций...")
        return result_list
    else:
        sort_rev_true_false = capitalize(input("Отсортировать 'по возрастанию' или 'по убыванию'?\n"))
        reverse_sort = True if sort_rev_true_false == "по убыванию" else False

        sorted_list = sorted(filtered_transact, key=lambda x: x["date"], reverse=reverse_sort)

        conclusion_rub_transact = capitalize(input("Выводить только рублевые транзакции? Да/Нет\n"))
        if conclusion_rub_transact == "Да":
            result_list = [t for t in sorted_list if t["currency_code"] == "RUB"]
        else:
            result_list = sorted_list

        if not result_list:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            return []

        print("Распечатываю итоговый список транзакций...")
        return result_list


def search_operation_excel(list_transact_3: list[dict], search_element: str):
    """Функция для подсчета количества банковских операций определенного типа, возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""
    print("Для обработки выбран XLSX-файл")
    while search_element not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции '{search_element}' недоступен")
        search_element = str(
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
        ).upper()

    df = pd.read_excel(list_transact_3, dtype=str, engine="openpyxl")
    transactions = df.to_dict(orient="records")

    filtered_transact = [i for i in transactions if re.search(search_element, str(i.get("state")))]
    print(f"Операции отфильтрованы по статусу '{search_element}'")
    if not filtered_transact:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return []

    sort_date = capitalize(input("Отсортировать операции по дате? Да/Нет\n"))
    if sort_date == "Да":
        sort_rev_true_false = capitalize(input("Отсортировать 'по возрастанию' или 'по убыванию'?\n"))
        reverse_sort = True if sort_rev_true_false == "по убыванию" else False

        sorted_list = sorted(filtered_transact, key=lambda x: x["date"], reverse=reverse_sort)

        conclusion_rub_transact = capitalize(input("Выводить только рублевые транзакции? Да/Нет\n"))
        if conclusion_rub_transact == "Да":
            result_list = [t for t in sorted_list if t["currency_code"] == "RUB"]
        else:
            result_list = sorted_list

        if not result_list:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            return []

        print("Распечатываю итоговый список транзакций...")
        return result_list
    else:
        sort_rev_true_false = capitalize(input("Отсортировать 'по возрастанию' или 'по убыванию'?\\n"))
        reverse_sort = True if sort_rev_true_false == "по убыванию" else False
        sorted_list = sorted(filtered_transact, key=lambda x: x["date"], reverse=reverse_sort)
        conclusion_rub_transacts = capitalize(input("Выводить только рублевые транзакции? Да/Нет\\n"))
        if conclusion_rub_transacts == "Да":
            results = [t for t in sorted_list if ["currency_code"] == ["RUB"]]
        else:
            results = sorted_list
        if results == []:
            print("Не найдено ни одной транзакции ,подходящей под ваши условия фильтрации")
            return []
        print("Распечатываю итоговый список транзакций...")
        return results


def count_category(list_transact: list[dict], list_for_count: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа, возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""
    result_list = []
    with open(list_transact, "r", encoding="utf-8") as f:
        data_1 = json.load(f)
        for transact in data_1:
            if transact.get("description") in list_for_count:
                result_list.append(transact["description"])
        counted = Counter(result_list)
        return counted


def result_search(format_file: int):
    search_element = str(
        input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
    ).upper()
    if format_file == 1:
        return search_operation_json(list_transact, search_element)
    else:
        if format_file == 2:
            return search_operation_csv(list_transact_2, search_element)
        else:
            if format_file == 3:
                return search_operation_excel(list_transact_3, search_element)
