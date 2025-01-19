import pandas as pd
import logging

logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/file_reader.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)

def excel_file_reader(file_way):
    """Функция принимает путь к файлу exel и выдаёт df"""
    try:
        df = pd.read_excel(file_way)
    except FileNotFoundError:
        logging.error(f"Файл не найден {file_way}")
    else:
        return df
