import json
import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.sort_transactions import (
    count_category,
    result_search,
    search_operation_csv,
    search_operation_excel,
    search_operation_json,
)


class TestOperations(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"state": "EXECUTED", "date": "2023-01-01", "operationAmount": {"currency": {"code": "RUB"}}}]',
    )
    @patch("builtins.input", side_effect=["EXECUTED", "Да", "по убыванию", "Да"])
    @patch("mypy.messages.capitalize", side_effect=lambda x: x)
    def test_search_operation_json_filter_and_sort(self, mock_capitalize, mock_input, mock_open):
        result = search_operation_json(["dummy"], "EXECUTED")
        if result is None:
            self.fail("Функция вернула None вместо списка")
        self.assertIsInstance(result, list)
        self.assertTrue(all(item["operationAmount"]["currency"]["code"] == "RUB" for item in result))

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["CANCELED", "Нет"])
    @patch("mypy.messages.capitalize", side_effect=lambda x: x)
    def test_search_operation_csv_filter_no_sort(self, mock_capitalize, mock_input, mock_open):
        csv_data = """id;state;date;amount;currency_name;currency_code;from;to
    1;CANCELED;2023-01-02;1000;RUB;RUB;A;B
    2;EXECUTED;2023-01-03;2000;USD;USD;A;B"""
        mock_open.return_value.read = lambda: csv_data

        result = search_operation_csv(["dummy"], "CANCELED")
        if result is None:
            self.fail("Функция вернула None вместо списка")
        self.assertIsInstance(result, list)
        self.assertTrue(all(item["state"] == "CANCELED" for item in result))
        mock_open.assert_called_once()

    @patch("pandas.read_excel")
    @patch("builtins.input", side_effect=["EXECUTED", "Да", "по возрастанию", "Нет"])
    @patch("mypy.messages.capitalize", side_effect=lambda x: x)
    def test_search_operation_excel_filter_and_sort(self, mock_capitalize, mock_input, mock_read_excel):
        df = pd.DataFrame(
            [
                {"id": "1", "state": "EXECUTED", "date": "2023-01-01", "amount": "1000"},
                {"id": "2", "state": "PENDING", "date": "2023-01-02", "amount": "2000"},
            ]
        )
        mock_read_excel.return_value = df

        result = search_operation_excel("dummy.xlsx", "EXECUTED")
        if result is None:
            self.fail("Функция вернула None вместо списка")
        self.assertIsInstance(result, list)
        self.assertTrue(all(item["state"] == "EXECUTED" for item in result))

    @patch("builtins.open", new_callable=mock_open)
    def test_count_category(self, mock_open):
        # Мок JSON данных
        data = [{"description": "category1"}, {"description": "category2"}, {"description": "category1"}]
        mock_open.return_value.read.return_value = json.dumps(data)

        count_result = count_category("dummy.json", ["category1"])
        self.assertEqual(count_result["category1"], 2)

    @patch("builtins.input")
    def test_result_search_json(self, mock_input):
        # Мокаем вызов input внутри функции result_search
        with patch("src.sort_transactions.search_operation_json") as mock_search:
            mock_search.return_value = ["result"]
            mock_input.return_value = "EXECUTED"
            result = result_search(1)
            self.assertEqual(result, ["result"])

    @patch("builtins.input")
    def test_result_search_csv(self, mock_input):
        with patch("src.sort_transactions.search_operation_csv") as mock_search:
            mock_search.return_value = ["csv_result"]
            mock_input.return_value = "CANCELED"
            result = result_search(2)
            self.assertEqual(result, ["csv_result"])

    @patch("builtins.input")
    def test_result_search_excel(self, mock_input):
        with patch("src.sort_transactions.search_operation_excel") as mock_search:
            mock_search.return_value = ["excel_result"]
            mock_input.return_value = "PENDING"
            result = result_search(3)
            self.assertEqual(result, ["excel_result"])

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"state": "CANCELED", "date": "2023-01-01", "operationAmount": {"currency": {"code": "RUB"}}}]',
    )
    @patch("builtins.input", side_effect=["EXECUTED", "Да", "по убыванию", "Нет"])
    @patch("mypy.messages.capitalize", side_effect=lambda x: x)
    def test_search_operation_json_no_matching_status(self, mock_capitalize, mock_input, mock_open):
        result = search_operation_json(["dummy"], "EXECUTED")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["CANCELED", "Нет"])
    @patch("mypy.messages.capitalize", side_effect=lambda x: x)
    def test_search_operation_csv_no_matching(self, mock_capitalize, mock_input, mock_open):
        csv_data = """id;state;date;amount;currency_name;currency_code;from;to
    1;EXECUTED;2023-01-02;1000;RUB;RUB;A;B
    2;EXECUTED;2023-01-03;2000;USD;USD;A;B"""
        mock_open.return_value.read = lambda: csv_data

        result = search_operation_csv(["dummy"], "CANCELED")
        self.assertEqual(result, [])

    @patch("pandas.read_excel")
    @patch("builtins.input", side_effect=["PENDING", "Нет"])
    @patch("mypy.messages.capitalize", side_effect=lambda x: x)
    def test_search_operation_excel_no_matching(self, mock_capitalize, mock_input, mock_read_excel):
        df = pd.DataFrame(
            [
                {"id": "1", "state": "EXECUTED", "date": "2023-01-01"},
                {"id": "2", "state": "CANCELED", "date": "2023-01-02"},
            ]
        )
        mock_read_excel.return_value = df

        result = search_operation_excel("dummy.xlsx", "PENDING")
        self.assertEqual(result, [])

    @patch(
        "builtins.open",
        new_callable=mock_open,
    )
    def test_count_category_no_descriptions(self, mock_open):
        data = [{"description": ""}, {"description": None}, {}]
        mock_open.return_value.read.return_value = json.dumps(data)

        result = count_category("dummy.json", ["category"])
        self.assertEqual(result["category"], 0)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"state": "CANCELED", "date": "2023-01-01", "operationAmount": {"currency": {"code": "RUB"}}}]',
    )
    @patch("builtins.input", side_effect=["EXECUTED", "Да", "по убыванию", "Нет"])
    @patch("mypy.messages.capitalize", side_effect=lambda x: x)
    def test_search_operation_json_no_matching_status(self, mock_capitalize, mock_input, mock_open):
        # Предположим, что функция возвращает пустой список при отсутствии совпадений
        result = search_operation_json(["dummy"], "EXECUTED")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_count_category_various_descriptions(self, mock_open):
        data = [{"description": "Food"}, {"description": "Transport"}, {"description": ""}, {"description": None}, {}]
        mock_open.return_value.read.return_value = json.dumps(data)
        result = count_category("dummy.json", ["Food", "Transport"])
        self.assertEqual(result.get("Food"), 1)
        self.assertEqual(result.get("Transport"), 1)

    @patch("builtins.open", new_callable=mock_open)
    def test_search_operation_json_empty_data(self, mock_open):
        mock_open.return_value.read.return_value = json.dumps([])
        result = search_operation_json(["dummy"], "EXECUTED")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_search_operation_json_malformed_data(self, mock_open):
        mock_open.return_value.read.return_value = "not a json"
        with self.assertRaises(json.JSONDecodeError):
            search_operation_json(["dummy"], "EXECUTED")

    @patch("builtins.open", new_callable=mock_open)
    def test_search_operation_json_no_matching_status_in_data(self, mock_open):
        mock_open.return_value.read.return_value = json.dumps(
            [{"state": "CANCELED", "date": "2023-01-01", "operationAmount": {"currency": {"code": "RUB"}}}]
        )
        result = search_operation_json(["dummy"], "EXECUTED")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_count_category_no_descriptions(self, mock_open):
        mock_open.return_value.read.return_value = json.dumps([{"description": ""}, {"description": None}, {}])
        result = count_category("dummy.json", ["category"])
        self.assertEqual(result["category"], 0)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_search_operation_json_file_not_found(self, mock_open):
        with self.assertRaises(FileNotFoundError):
            search_operation_json(["dummy"], "EXECUTED")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_count_category_file_not_found(self, mock_open):
        with self.assertRaises(FileNotFoundError):
            count_category("dummy.json", ["category"])

    @patch("pandas.read_excel")
    def test_search_operation_excel_empty_df(self, mock_read_excel):
        df_empty = pd.DataFrame()
        mock_read_excel.return_value = df_empty
        result = search_operation_excel("dummy.xlsx", "EXECUTED")
        self.assertEqual(result, [])
