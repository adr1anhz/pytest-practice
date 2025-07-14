import pytest

def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False
    
@pytest.mark.parametrize("n, expected", [
    (1, False),
    (2, True),
    (3, False),
    (4, True)
])

def test_is_even(n, expected):
    assert is_even(n) == expected