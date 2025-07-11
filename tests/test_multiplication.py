import pytest

# Multiplication test ideas:
# two positive integers
# identity: multiply by 1
# zero: multiply by 0
# positive by negative
# negative by negative
# floats


products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product