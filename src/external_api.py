import os
from typing import Any

import requests
import logging

logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/file_reader.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)

def currency_conversion(source: str) -> Any:
    """Запрос курса валюты в рублях API"""
    payload: dict = {}
    url = f"https://api.apilayer.com/currency_data/live?source={source}&cies=RUB"
    headers = {"apikey": os.getenv("API_KEY_APILAYER")}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except requests.exceptions.RequestException:
        logging.error("Произошла ошибка. Пожалуйста, повторите попытку позже.")
    else:
        logging.info("Всё ок")
        return response.json()["quotes"][f"{source}RUB"]


def stock_prices(symbols: str) -> Any:
    """"""
    url = f"https://api.marketstack.com/v1/eod?access_key={os.getenv('API_KEY')}"
    querystring = {"symbols": f"{symbols}"}
    try:
        response = requests.get(url, params=querystring)
    except requests.exceptions.RequestException:
        logging.error("Произошла ошибка. Пожалуйста, повторите попытку позже.")
    else:
        logging.info("Всё ок")
        return response.json()["data"][0]["close"]
