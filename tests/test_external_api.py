from unittest.mock import patch

from src.external_api import conversion_func

transaction_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

transaction_usd = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


# Тест на корректную работу функции когда на вход подается транзакция в валюте RUB
@patch("requests.request")
def test_conversion_func_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 31957.58}
    assert conversion_func(transaction_rub) == 31957.58
    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=RUB&amount=31957.58",
        headers={"apikey": "f5nyr0yF5s7ILP2eHKURQFFsR65627Sn"},
        data={},
    )


# {'to':'RUB', 'from':'RUB', 'amount':'31957.58'}
# 'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=RUB&amount=31957.58'


# Тест на корректную работу функции когда на вход подается транзакция в валюте USD
@patch("requests.request")
def test_conversion_func_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 2947786.162003}
    assert conversion_func(transaction_usd) == 2947786.162003
    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=31957.58",
        headers={"apikey": "f5nyr0yF5s7ILP2eHKURQFFsR65627Sn"},
        data={},
    )
