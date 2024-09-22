#Проект "Виджет банковских операций"

##Описание:
Это виджет, который показывает несколько последних успешных банковских операций клиента. Проект готовит данные для отображения в новом виджете.
- Реализована функция, которая принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате 
XXXX XX** **** XXXX, где X — это цифра номера
- Реализована функция, которая принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате 
**XXXX, где X — это цифра номера.
- Реализована функция, которая принимает один аргумент — строку, содержащую тип и номер карты или счета и возвращает строку с замаскированным номером. 
Для карт и счетов используются разные типы маскировки. 
- Реализована функция, которая  принимает на вход строку с датой в формате 
"2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
- Реализована функция, которая принимает список словарей и опционально значение для ключа 
и возвращает новый список словарей, содержащий только те словари, у которых ключ соответствует указанному значению.
- Реализована функция, которая принимает список словарей и порядок сортировки (по умолчанию — убывание) 
и возвращает новый список, отсортированный по дате.
- Реализована функция,которая принимает на вход список словарей, представляющих транзакции 
и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
- Реализована функция,которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
- Реализована функция,которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
- Создан декоратор log, который автоматически логирует начало и конец выполнения функции, 
а также ее результаты или возникшие ошибки в консоль или файл.
- Реализована функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
- Реализована функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях
##Установка:
1.Клонируйте репозиторий:
```
git@github.com:Julia-Nafikova/Homework_10_1.git
```

2.Установите зависимости:
```
poetry install
```
##Тестирование
* Добавлены тесты модуля masks
* Добавлены тесты модуля widget
* Добавлены тесты модуля processing
* Добавлены тесты модуля generators
* Добавлены тесты модуля decorators
* Добавлены тесты модуля utils
* Добавлены тесты модуля external_api

Покрытие тестами 98%

##Использование:

##Документация: