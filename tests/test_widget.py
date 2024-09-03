import pytest

from src.widget import mask_account_card, get_date

@pytest.fixture
def numbers():
    return 'Visa Platinum 7000 79** **** 6361'

@pytest.mark.parametrize('numbers, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                               ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                               ('Счет 64686473678894779589', 'Счет **9589'),
                                               ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                               ('', 'Ошибка ввода')
                                               ])

def test_mask_account_card(numbers, expected):
    assert mask_account_card(numbers) == expected


@pytest.fixture
def date():
    return '11.03.2024'

@pytest.mark.parametrize('date, expected', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                            ('', 'Ошибка ввода')
                                            ])

def test_get_date(date, expected):
    assert get_date(date) == expected
