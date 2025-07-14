import pytest


class Calculator():
    def add(self, a, b):
        return a + b
    


@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-3, 5, 2),
    (-2, -4, -6)
])


def test_add_param(calc, a, b, expected):
    assert calc.add(a, b) == expected

