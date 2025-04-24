import os

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction: dict) -> float:
    """Функция, которая возвращает сумму транзакции в рублях."""
    load_dotenv()
    api_key = os.getenv("API_KEY")
    header = {"apikey": api_key}
    amount = transaction.get("operationAmount").get("amount")
    conv_from = transaction.get("operationAmount").get("currency").get("code")
    url = f" https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={conv_from}&amount={amount}"
    if conv_from == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        result = requests.get(url, headers=header).json()
        return round(float(result.get("result")), 2)
