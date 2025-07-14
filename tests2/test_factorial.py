import pytest


def factorial(n):
    if n < 0:
        raise ValueError("Liczba nie może być ujemna")
    wynik = 1
    for i in range (1, n + 1):
        wynik *= i
    return wynik





@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120),
])


def test_factorial_valid(n, expected):
    assert factorial(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)