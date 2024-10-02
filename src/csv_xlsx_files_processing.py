# -*- coding: utf-8 -*-
import csv
import json

import pandas as pd


def get_data_csv(path):
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


print(get_data_csv("../data/transactions.csv"))


def get_data_excel(path):
    """Функция считывает финансовые операции из Excel файла и выдает список словарей с транзакциями"""
    result = pd.read_excel(path).to_json(orient="records", indent=4, force_ascii=False)
    return json.loads(result)


# print(get_data_excel("../data/transactions_excel.xlsx"))