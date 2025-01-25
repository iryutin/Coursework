import datetime
import logging
from typing import Optional

import pandas as pd

from src.config import LOG_FOLDER
from src.decorators import log

logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{LOG_FOLDER}/reports.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


@log('reports')
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    if date is None:
        date_new = datetime.datetime.now()
    else:
        try:
            date_new = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            logging.error(f"Неверный формат даты{date} должно быть %Y-%m-%d %H:%M:%S")
        else:
            logging.info("Дата ок")
    date_beginning = date_new - datetime.timedelta(weeks=10)
    date_beginning = date_beginning.replace(day=1)
    data_filter_date = transactions[
        (date_new.strftime("%d.%m.%Y %H:%M:%S") > transactions["Дата операции"])
        & (transactions["Дата операции"] > date_beginning.strftime("%d.%m.%Y %H:%M:%S"))
    ]
    df_data_operations_pay = data_filter_date[data_filter_date["Сумма операции"] < 0]
    date_operations_pay_by_categories = df_data_operations_pay[df_data_operations_pay["Категория"] == category]
    logging.info("Всё ок")
    return date_operations_pay_by_categories


# print(spending_by_category(excel_file_reader("D:/coursework_1/pythonProject1/data/operation.xls"), "Фастфуд"))
