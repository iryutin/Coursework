import datetime

import pandas as pd

from src.views import get_cards, get_greeting, get_top_transactions


def test_get_greeting():
    assert get_greeting(6) == "Доброе утро"
    assert get_greeting(12) == "Добрый день"
    assert get_greeting(18) == "Добрый вечер"
    assert get_greeting(0) == "Доброй ночи"


def test_get_cards(test_dataframe):
    df_test = pd.DataFrame(test_dataframe)
    data_time = "2025-01-20 00:00:00"
    date_obj = datetime.datetime.strptime(data_time, "%Y-%m-%d %H:%M:%S")
    answer = [
        {
            "last_digits": "*0473",
            "total_spent": float("2570"),
            "cashback": float("0"),
        },
        {
            "last_digits": "*8164",
            "total_spent": float("3973"),
            "cashback": float("10"),
        },
    ]
    assert get_cards(df_test, date_obj) == answer


def test_get_top_transactions(test_dataframe):
    df_test = pd.DataFrame(test_dataframe)
    data_time = "2025-01-20 00:00:00"
    date_obj = datetime.datetime.strptime(data_time, "%Y-%m-%d %H:%M:%S")
    answer = [
        {
            "last_digits": "*8164",
            "total_spent": float("3973"),
            "cashback": float("10"),
        },
        {
            "last_digits": "*0473",
            "total_spent": float("2570"),
            "cashback": float("0"),
        },
    ]
    assert get_top_transactions(df_test, date_obj) == answer
