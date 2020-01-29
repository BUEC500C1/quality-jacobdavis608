# Sample test script to understand CI
import sys
sys.path.insert(1, '../')

from num_convert.num_convert import *

def test_single_digit():
    assert convert_to_rom(0) == ""
    assert convert_to_rom(1) == "I"
    assert convert_to_rom(2) == "II"
    assert convert_to_rom(3) == "III"
    assert convert_to_rom(4) == "IV"
    assert convert_to_rom(5) == "V"
    assert convert_to_rom(6) == "VI"
    assert convert_to_rom(7) == "VII"
    assert convert_to_rom(8) == "VIII"
    assert convert_to_rom(9) == "IX"

def test_random():
    assert convert_to_rom(20) == "XX"
    assert convert_to_rom(203) == "CCIII"
    assert convert_to_rom(2751) == "MMDCCLI"
    assert convert_to_rom(5751) == "(V)DCCLI"
    assert convert_to_rom(100000) == "(C)"
    assert convert_to_rom(100600) == "(C)DC"
    assert convert_to_rom(601040) == "(D)(C)MXL"