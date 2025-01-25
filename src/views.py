import datetime
import json
import logging

from pandas import DataFrame

from src.config import DATA_USER_SETTINGS, LOG_FOLDER
from src.external_api import currency_conversion, stock_prices

logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{LOG_FOLDER}/views.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_greeting(time: int) -> str:
    """Принимает актуальное время и выдаёт приветствие"""
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


def get_cards(df_data_operations: DataFrame, date_now: datetime.datetime) -> list[dict]:
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


def get_top_transactions(df_data_operations: DataFrame, date_now: datetime.datetime) -> list[dict]:
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
    """Удобно формирует ответ по курсу валюте настройка идёт через файл user_settings.json"""
    with open(DATA_USER_SETTINGS) as f:
        data = json.load(f)
    result = []
    for data_currency in data["user_currencies"]:
        result.append({"currency": data_currency, "rate": currency_conversion(data_currency)})
    return result


def get_stock_prices() -> list[dict]:
    """Удобно формирует курсы указанных акций настройка идёт через файл user_settings.json"""
    with open(DATA_USER_SETTINGS) as f:
        data = json.load(f)
    result = []
    for data_stocks in data["user_stocks"]:
        result.append({"stock": data_stocks, "price": stock_prices(data_stocks)})
    return result


# file = os.getenv('DATA_FILE')
# print(file)
# date_obj = datetime.datetime.now()
# data = get_cards(excel_file_reader(file), date_obj)
# print(get_top_transactions(excel_file_reader(file),date_obj))
# print(get_currency_conversion())
# print(get_stock_prices())
