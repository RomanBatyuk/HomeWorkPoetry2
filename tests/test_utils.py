import json
from unittest.mock import MagicMock, mock_open, patch

from src.utils import download_file_from_google_drive


def test_download_file_from_google_drive():
    """Тест успешной загрузки и чтения файла"""
    test_data = [{"id": 1, "amount": 100}]

    with (
        patch("gdown.download"),
        patch("os.path.exists", MagicMock(return_value=True)),
        patch("builtins.open", mock_open(read_data=json.dumps(test_data))),
    ):
        result = download_file_from_google_drive("test_id", "test_output")
        assert result == test_data


def test_download_file_from_google_drive_1():
    """Тест отработки условия, если читаемый файл пустой"""
    test_data = []

    with (
        patch("gdown.download"),
        patch("os.path.exists", MagicMock(return_value=True)),
        patch("builtins.open", mock_open(read_data=json.dumps(test_data))),
    ):
        result = download_file_from_google_drive("test_id", "test_output")
        assert result == test_data
