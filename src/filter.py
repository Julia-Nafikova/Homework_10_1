# -*- coding: utf-8 -*-

from src.utils import read_file_json
from collections import Counter
import re


def filter_word(list_filter: list, option: str) -> list:
    """Функция фильтрует список по заданному значению в описании"""
    new_list_filter = []
    for i in list_filter:
        if "description" in i and re.search(option, i["description"], flags=re.IGNORECASE):
            new_list_filter.append(i)
        return new_list_filter


def filter_category(list_filter: list, list_category: list) -> dict:
    """Функция фильтрует список по категориям и возвращает количество операций по категориям"""
    new_list = []
    for i in list_filter:
        if "description" in i:
            if i["description"] in list_category:
                new_list.append(i["description"])
    counted = Counter(new_list)
    return counted


ret = read_file_json("./data/operations.json")

category = ["Перевод организации", "Открытие вклада", "Перевод с карты на карту", "Перевод с карты на счет"]

# print(filter_word(ret, "Перевод организации"))
# print(filter_category(ret, category))
