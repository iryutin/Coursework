import datetime

import pandas as pd

from src.external_api import currency_conversion, stock_prices
import logging

logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/file_reader.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_greeting(time: int) -> str:
    logging.info("Начало работы функции")
    greeting = ""
    if time in range(6, 12):
        greeting = "Доброе утро"
    elif time in range(12, 18):
        greeting = "Добрый день"
    elif time in range(18, 24):
        greeting = "Добрый вечер"
    elif time in range(0, 6):
        greeting = "Доброй ночи"
    logging.info("Всё ок")
    return greeting


def get_cards(df_data_operations: pd.core.frame.DataFrame, date_now: datetime) -> list[dict]:
    """Принемает датафрем фильтрует по дате и списанию затем выдаёт словарь с суммой расходов, кэшбэком по картам"""
    logging.info("Начало работы функции")
    date_beginning = date_now.replace(day=1, hour=0, minute=0, second=0)
    df_data_operations_by_date = df_data_operations[
        (date_now.strftime("%d.%m.%Y %H:%M:%S") > df_data_operations["Дата операции"])
        & (df_data_operations["Дата операции"] > date_beginning.strftime("%d.%m.%Y %H:%M:%S"))
    ]
    df_data_operations_pay = df_data_operations_by_date[df_data_operations_by_date["Сумма операции"] < 0]
    df_data_operations_pay = df_data_operations_pay.groupby("Номер карты").sum()
    df_data_operations_pay = df_data_operations_pay.loc[:, ["Сумма операции", "Кэшбэк"]]
    df_card_head = df_data_operations_pay.head()
    cards_namber = []
    for card in df_card_head.index.values:
        cards_namber.append(
            {
                "last_digits": f"{card}",
                "total_spent": float(df_data_operations_pay.loc[card, "Сумма операции"]) * -1,
                "cashback": float(df_data_operations_pay.loc[card, "Кэшбэк"]),
            }
        )
    logging.info("Всё ок")
    return cards_namber


def get_top_transactions(df_data_operations: pd.core.frame.DataFrame, date_now: datetime) -> list[dict]:
    """Принемает датафрем фильтрует по дате и списанию затем выдаёт словарь с топ 5 расходов, кэшбэком по картам"""
    logging.info("Начало работы функции")
    date_beginning = date_now.replace(day=1, hour=0, minute=0, second=0)
    df_data_operations_by_date = df_data_operations[
        (date_now.strftime("%d.%m.%Y %H:%M:%S") > df_data_operations["Дата операции"])
        & (df_data_operations["Дата операции"] > date_beginning.strftime("%d.%m.%Y %H:%M:%S"))
    ]
    df_data_operations_pay = df_data_operations_by_date[
        (df_data_operations_by_date["Сумма операции"] < 0) & (df_data_operations_by_date["Номер карты"] is not None)
    ]
    df_data_operations_pay = df_data_operations_pay.sort_values("Сумма операции")
    df_data_operations_pay = df_data_operations_pay.loc[:, ["Номер карты", "Сумма операции", "Кэшбэк"]]
    df_data_operations_pay = df_data_operations_pay.dropna()
    df_data_operations_top = df_data_operations_pay.iloc[0:5, :]
    data_operations_top = df_data_operations_top.head()
    top_transaction = []
    for operations_namber in data_operations_top.index.values:
        top_transaction.append(
            {
                "last_digits": df_data_operations_top.loc[operations_namber, "Номер карты"],
                "total_spent": float(df_data_operations_top.loc[operations_namber, "Сумма операции"]) * -1,
                "cashback": float(df_data_operations_top.loc[operations_namber, "Кэшбэк"]),
            }
        )
    logging.info("Всё ок")
    return top_transaction


def get_currency_conversion() -> list[dict]:
    """Удобно формирует ответ по курсу валюте"""
    return [
        {"currency": "USD", "rate": currency_conversion("USD")},
        {"currency": "EUR", "rate": currency_conversion("EUR")},
    ]


def get_stock_prices() -> list[dict]:
    """Удобно формирует курсы указанных акций"""
    return [
        {"stock": "AAPL", "price": stock_prices("AAPL")},
        {"stock": "AMZN", "price": stock_prices("AMZN")},
        {"stock": "GOOGL", "price": stock_prices("GOOGL")},
        {"stock": "MSFT", "price": stock_prices("MSFT")},
        {"stock": "TSLA", "price": stock_prices("TSLA")},
    ]


# file = os.getenv('DATA_FILE')
# print(file)
# date_obj = datetime.datetime.now()
# data = get_cards(excel_file_reader(file), date_obj)
# print(get_top_transactions(excel_file_reader(file),date_obj))
# print(get_currency_conversion())
# print(get_stock_prices())
