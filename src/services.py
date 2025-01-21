import datetime
import json
from json import JSONDecoder, JSONEncoder

from pandera.typing import DataFrame


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
    return json.dumps(date_final, ensure_ascii=False)
