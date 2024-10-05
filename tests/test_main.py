import pytest

from main import multiplying_numbers, repeating_letter

@pytest.fixture
def coll():
    return ["mom", "like", "apple"]

def test_repeating_letter(coll):
    assert repeating_letter(coll) == ["mom"]

    assert repeating_letter([]) == []

    with pytest.raises(TypeError):
        assert repeating_letter(1) == []

        assert repeating_letter(True) == []


@pytest.mark.parametrize("list_number, mult", [([1, 2, 3], 6), ([5, 5, 4], 25), ([10, 10, 9], 100)])
def test_nums(list_number, mult):
    assert multiplying_numbers(list_number) == mult
