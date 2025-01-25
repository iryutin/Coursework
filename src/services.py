import datetime
import json
import logging

from pandas import DataFrame

logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/file_reader.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def category_cashback(data: DataFrame, year: int, month: int) -> str:
    """Принимает датафрейм и фильтрует по категориям кэшбека"""
    date_now = datetime.datetime(year=year, month=month, day=30)
    date_beginning = date_now.replace(day=1, hour=0, minute=0, second=0)
    data_filter_date = data[
        (date_now.strftime("%d.%m.%Y %H:%M:%S") > data["Дата операции"])
        & (data["Дата операции"] > date_beginning.strftime("%d.%m.%Y %H:%M:%S"))
    ]
    date_cashback_categories = data_filter_date.loc[:, ["Кэшбэк", "Категория"]]
    date_grupe_cashback_categories = date_cashback_categories.groupby("Категория").sum()
    date_final = date_grupe_cashback_categories.to_dict()
    date_final = date_final["Кэшбэк"]
    logging.info("Всё ок")
    return json.dumps(date_final, ensure_ascii=False)
