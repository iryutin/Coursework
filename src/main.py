import datetime
import json
import os

from external_api import currency_conversion
from src.file_rider import excel_file_reader
from views import get_cards, get_currency_conversion, get_greeting, get_stock_prices, get_top_transactions


def main(data_time):
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


print(main("2025-01-17 00:00:00"))
