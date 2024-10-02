# -*- coding: utf-8 -*-
import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/file.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def read_file(path):
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


print(read_file("../data/operations.json"))

# with open(path, encoding='utf-8') as f:
# fh = logging.FileHandler('log.txt', encoding='utf-8')
