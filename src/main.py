import datetime
import json
import os

from dotenv import load_dotenv
from src.services import category_cashback
from src.file_rider import excel_file_reader
from src.views import get_cards, get_currency_conversion, get_greeting, get_stock_prices, get_top_transactions
from src.reports import spending_by_category
load_dotenv()


def main(data_time: str) -> str:
    """Основная функция принимает дату и выдаёт данные трат с карт,
    топ трат курсы валют и стоимость акций в данном месяце в json формате"""
    date_obj = datetime.datetime.strptime(data_time, "%Y-%m-%d %H:%M:%S")
    file = os.getenv("DATA_FILE")
    cards_namber = get_cards(excel_file_reader(file), date_obj)
    top_transactions = get_top_transactions(excel_file_reader(file), date_obj)
    answer = {
        "greeting": f"{get_greeting(date_obj.hour)}",
        "cards": cards_namber,
        "top_transactions": top_transactions,
        "currency_rates": get_currency_conversion(),
        "stock_prices": get_stock_prices(),
    }
    return json.dumps(answer, ensure_ascii=False)


#Вызов функции Вэб страница
date = input("Введите дату формат %Y-%m-%d %H:%M:%S")
main(date)

#Вызов функции Сервисы
year = int(input("Введите год"))
month: int(input("Введите месяц"))
file_operatin = excel_file_reader(os.getenv("DATA_FILE"))
print(category_cashback(file_operatin, year, month))

#Вызов отчёта
date = input("Введите дату формат %Y-%m-%d %H:%M:%S")
category = input("Ввидите категорию")
spending_by_category(file_operatin, category, date)
