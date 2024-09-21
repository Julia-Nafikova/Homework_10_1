import json


def read_file(path):
    transaction_data = []
    try:
        with open(path, encoding='utf-8') as f:
            transaction_data = json.load(f)
    except json.JSONDecodeError:
        print("Invalid JSON data.")
    except FileNotFoundError as e:
        print(e)
    return transaction_data

# print(read_file('../data/operation.json'))