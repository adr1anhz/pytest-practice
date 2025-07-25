import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from stuff.accum import Accumulator

@pytest.mark.accumulator
def accum():
    return Accumulator()

@pytest.mark.accumulator
def test_accumulator_init(accum, accum2):
    assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

@pytest.mark.accumulator
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10