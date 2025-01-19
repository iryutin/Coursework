import datetime
import os

from src.file_rider import excel_file_reader
from dotenv import load_dotenv

def greeting (time:int) -> str:
    if time in [6,12]:
        return 'Доброе утро'
    elif time in [12,18]:
        return 'Добрый день'
    elif time in [18, 24]:
        return 'Добрый вечер'
    elif time in [0, 6]:
        return 'Доброй ночи'

def cards(df_data_operations, date_now) -> list[dict]:
    """Принемает датафрем фильтрует по дате и списанию затем выдаёт словарь с суммой расходов по картам"""
    print(df_data_operations)
    date_beginning = date_now.replace(day=1, hour=0, minute = 0, second = 0)
    df_data_operations_by_date = df_data_operations[(date_now.strftime("%d.%m.%Y %H:%M:%S")>df_data_operations['Дата операции']) & (df_data_operations['Дата операции']>date_beginning.strftime("%d.%m.%Y %H:%M:%S"))]
    print(df_data_operations_by_date)
    df_data_operations_pay = df_data_operations_by_date[df_data_operations_by_date['Сумма операции']<0]
    df_data_operations_pay = df_data_operations_pay.groupby('Номер карты').sum()
    df_data_operations_pay = df_data_operations_pay.loc[:,['Сумма операции']]
    print(df_data_operations_pay)

file = os.getenv('DATA_FILE')
print(file)
#date_obj = datetime.datetime.now()
#cards(excel_file_reader(file), date_obj)