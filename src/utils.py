import json
import logging

import gdown

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="logs/utils.log",
    filemode="w",
    encoding="utf-8",
)

utils_logger = logging.getLogger("utils")


file_id = "1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy"
output = "data/operations.json"


def download_file_from_google_drive(file_id: str, output: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    utils_logger.info("Получение данных для работы функции")
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=False)
    utils_logger.info(f"Запись полученных данных {output}")
    with open("data/operations.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        utils_logger.info("Загрузка данных из файла в формате JSON и преобразование их в объект Python")
        if not isinstance(data, list) or len(data) == 0:
            utils_logger.info(f"Функция возвращает пустой список, если {output} пуст или не является списком")
            return []
        else:
            utils_logger.info("Результат работы функции download_file_from_google_drive получен")
            return data


if __name__ == "__main__":
    file_id = "1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy"
    output = "data/operations.json"
    print(download_file_from_google_drive(file_id, output))
