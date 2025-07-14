import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Nie mozna dzielic przez zero")
    return a / b


@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (10, 5, 2),
    (8, 4, 2),
])

def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(5, 0)
    assert str(exc_info.value) == "Nie mozna dzielic przez zero"