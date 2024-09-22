from unittest.mock import patch, mock_open

from src.utils import read_file


# Тест на корректный файл с трансзакциями
@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_valid_file(mock_file):
    transaction = read_file("../data/operations.json")
    assert transaction == [{"amount": 100, "currency": "USD"}]


# Tecт на пустой файл
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file):
    transaction = read_file("../data/operations.json")
    assert transaction == []


# Тест на некорректный тип данных(не список)
@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
def test_not_list(mock_file):
    transaction = read_file("../data/operations.json")
    assert transaction == {"amount": 100, "currency": "USD"}


# Если файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    transaction = read_file("../data/operations.json")
    assert transaction == []
