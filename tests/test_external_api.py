from unittest.mock import patch

from src.external_api import get_transaction_amount


@patch("requests.get")
def test_get_transaction_amount_requests(mock_test):
    """Тест возврата суммы транзакции"""
    mock_test.return_value.json.return_value = {"result": "12.13332"}
    assert (
        get_transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
            }
        )
        == 12.13
    )
