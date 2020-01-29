# Sample test script to understand CI
import sys
sys.path.insert(1, '../')

from num_convert.num_convert import *


def test_simple():
    assert 1 == 1
    arabic = [1, 2, 3, 4]

    assert convert_to_rom(arabic) == 4
