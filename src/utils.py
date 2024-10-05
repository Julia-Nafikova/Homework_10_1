# -*- coding: utf-8 -*-
import json
import logging
import csv
import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="./logs/file.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def read_file_json(path):
    transaction_data = []
    try:
        logger.info("Открытие файла по указанному пути")
        with open(path, encoding="utf-8") as f:
            logger.info("Преобразование json-данных из файла")
            transaction_data = json.load(f)
    except json.JSONDecodeError:
        logger.warning("Ошибка: некорректные данные")
        print("Invalid JSON data.")
    except FileNotFoundError as e:
        logger.error("Ошибка: Некорректный путь к файлу, либо файл отсутствует")
        print(e)
    return transaction_data


# print(read_file_json("../data/operations.json"))

# with open(path, encoding='utf-8') as f:
# fh = logging.FileHandler('log.txt', encoding='utf-8')


def read_file_csv(path):
    """Функция считывает финансовые операции из CSV файла и выдает список словарей с транзакциями"""
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = dict()
            for i, item in enumerate(header):
                row_dict[item] = row[i]
            result.append(row_dict)
    return result


# print(read_file_csv("../data/transactions.csv"))


def read_file_excel(path):
    """Функция считывает финансовые операции из Excel файла и выдает список словарей с транзакциями"""
    result = pd.read_excel(path).to_json(orient="records", indent=4, force_ascii=False)
    return json.loads(result)


# print(read_file_excel("../data/transactions_excel.xlsx"))
