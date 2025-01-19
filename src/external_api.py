import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


def currency_conversion(source:str) -> float:
    """Запрос курса валюты в рублях API"""
    payload = {}
    url = f"https://api.apilayer.com/currency_data/live?source={source}&cies=RUB"
    headers = {"apikey": os.getenv("API_KEY_APILAYER")}
    response = requests.request("GET", url, headers=headers, data = payload)
    return response.json()["quotes"][f"{source}RUB"]

def stock_prices(symbols):
    """"""
    url = f"https://api.marketstack.com/v1/eod?access_key={os.getenv('API_KEY')}"
    querystring = {"symbols": f"{symbols}"}
    response = requests.get(url, params=querystring)
    return response.json()["data"][0]["close"]