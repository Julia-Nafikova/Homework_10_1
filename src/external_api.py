import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY=os.getenv('API_KEY')

payload = {}
headers= {
  "apikey": API_KEY
}

def conversion_func(transaction):
    currency_code_to = 'RUB'
    currency_code_from = transaction['operationAmount']['currency']['code']
    amount = transaction['operationAmount']['amount']
    url = f'https://api.apilayer.com/exchangerates_data/convert?to={currency_code_to}&from={currency_code_from}&amount={amount}'
    if currency_code_from == 'USD' or 'EUR':
        response = requests.request("GET", url, headers=headers, data = payload)
        result = response.json()['result']
        return result
    else:
        return amount

# print(conversion_func({
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   }))




