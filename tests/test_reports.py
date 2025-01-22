import pandas as pd

from src.reports import spending_by_category


def test_spending_by_category(test_dataframe):
    transactions = pd.DataFrame(test_dataframe)
    test_df = pd.DataFrame(
        [
            {
                "Дата операции": "18.01.2025 14:11:38",
                "Номер карты": "*0473",
                "Сумма операции": -2570,
                "Кэшбэк": 0,
                "Категория": "Фастфуд",
            }
        ]
    )
    df = spending_by_category(transactions, "Фастфуд")
    assert df.equals(test_df)
