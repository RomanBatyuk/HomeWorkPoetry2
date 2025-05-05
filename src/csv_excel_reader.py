import csv

import pandas as pd


def scv_reader(path: str) -> list[dict]:
    """Функция приниммает путь к файлу csv и возвращает список словарей с транзакциями"""
    transactions = []
    with open(path, "r", encoding="utf-8") as file:
        df = csv.DictReader(file, delimiter=";")
        for row in df:
            dict_transact = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "amount": row["amount"],
                "currency_name": row["currency_name"],
                "currency_code": row["currency_code"],
                "from": row["from"],
                "to": row["to"],
            }
            transactions.append(dict_transact)
        return transactions


def excel_reader(path: str) -> list[dict]:
    """Функция приниммает путь к файлу excel и возвращает список словарей с транзакциями"""
    transactions = []
    df = pd.read_excel(path, dtype=str, engine="openpyxl")
    transactions = df.to_dict(orient="records")
    return transactions
