from unittest.mock import patch

import pandas as pd

from src.file_rider import excel_file_reader


@patch("pandas.read_excel")
def test_excel_file_reader(mock_get):
    """Тест функции excel_file_reader"""
    mock_get.return_value = pd.DataFrame(
        {
            "id": 441945886,
            "state": ["EXECUTED"],
            "date": ["2019-08-26T10:50:58.294041"],
            "amount": ["31957.58"],
            "currency_name": ["руб."],
            "currency_code": ["RUB"],
            "description": ["Перевод организации"],
            "from": ["Maestro 1596837868705199"],
            "to": ["Счет 64686473678894779589"],
        }
    )
    test_df = pd.DataFrame(
        {
            "id": 441945886,
            "state": ["EXECUTED"],
            "date": ["2019-08-26T10:50:58.294041"],
            "amount": ["31957.58"],
            "currency_name": ["руб."],
            "currency_code": ["RUB"],
            "description": ["Перевод организации"],
            "from": ["Maestro 1596837868705199"],
            "to": ["Счет 64686473678894779589"],
        }
    )
    df = excel_file_reader("")
    assert df.equals(test_df)
