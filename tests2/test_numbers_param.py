import pytest

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False
    

@pytest.mark.parametrize("a, expected", [
    (1, True),
    (2, False),
    (3, True),
    (4, False)
])

def test_numbers_param(a, expected):
    assert is_odd(a) == expected