import json

import gdown

file_id = "1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy"
output = "data/operations.json"


def download_file_from_google_drive(file_id, output):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=False)
    with open("data/operations.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        if not isinstance(data, list) or len(data) == 0:
            return []
        else:
            return data


print(download_file_from_google_drive(file_id, output))

if __name__ == "__main__":
    file_id = "1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy"
    output = "data/operations.json"
    print(download_file_from_google_drive(file_id, output))
