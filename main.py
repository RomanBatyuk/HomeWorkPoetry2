from src.sort_transactions import result_search, count_category

list_transact = "data/data.json"
list_transact_2 = "transactions/transactions.csv"
list_transact_3 = "transactions/transactions_excel.xlsx"

def main():
    format_file = int(
        input(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n"
        )
    )
    print(result_search(format_file))
    list_for_count = [str.capitalize(i) for i in input("Введите категорию или категории операции\n(Пример: Перевод с карты на карту, Открытие вклада, Перевод организации)\n").split(", ")]
    print(count_category(list_transact, list_for_count))



if __name__=="__main__":
    main()