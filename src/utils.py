import json


def read_file(path):
    with open(path, encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Invalid JSON data.")
        except FileNotFoundError as e:
            print(e)

        return data

transaction_data = read_file('../data/operations.json')