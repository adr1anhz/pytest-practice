import pytest

@pytest.mark.parametrize("a, b, result", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_addition(a, b, result):
    assert a + b == result