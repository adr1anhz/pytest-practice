import pytest

class Calculator:
    def add(self, a, b):
        return a + b
    def substract(self, a, b):
        return a - b
    
@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_subtract(calc):
    assert calc.substract(5, 1) == 4