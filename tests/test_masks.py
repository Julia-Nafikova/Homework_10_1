import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_number() -> None:
    return


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("700079228960636112", "Ошибка ввода"),
        ("67543821", "Ошибка ввода"),
        ("aujsgtfdnclo", "Ошибка ввода"),
        ("", "Ошибка ввода"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.fixture
def acc_number() -> None:
    return


@pytest.mark.parametrize(
    "acc_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("2345615789532145876521", "Ошибка ввода"),
        ("67543821", "Ошибка ввода"),
        ("5au1j2s45gtfd12nclo3", "Ошибка ввода"),
        ("", "Ошибка ввода"),
    ],
)
def test_get_mask_account(acc_number: str, expected: str) -> None:
    assert get_mask_account(acc_number) == expected
