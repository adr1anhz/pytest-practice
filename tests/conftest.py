import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum(scope='function'):
    yield Accumulator()
    print("Done with the test!")

@pytest.fixture
def accum2():
    return Accumulator()
