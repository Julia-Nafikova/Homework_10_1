import json


def read_file(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        return data

print(read_file('../data/operations.json'))