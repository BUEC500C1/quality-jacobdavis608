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

def test_easy_input():
    assert convert_to_rom(20) == "XX"
    assert convert_to_rom(203) == "CCIII"
    assert convert_to_rom(2751) == "MMDCCLI"
    assert convert_to_rom(5751) == "(V)DCCLI"
    assert convert_to_rom(100000) == "(C)"
    assert convert_to_rom(100600) == "(C)DC"
    assert convert_to_rom(601040) == "(D)(C)MXL"

def test_random_input():
    assert convert_to_rom("20") == "N/A"
    assert convert_to_rom(203.443) == "N/A"
    assert convert_to_rom("2751") == "N/A"

    # pass it a list
    arabic_nums = [1, 2, 3, 4]
    assert convert_to_rom(arabic_nums) == "N/A"

    #pass it a dictionary
    arabic_dict = {1: "hello", 2: "testing", 3: "1,2"}
    assert convert_to_rom(arabic_dict) == "N/A"

def test_high_magnitude():
    #pass too high a magnitude
    assert convert_to_rom(100000000) == "N/A"