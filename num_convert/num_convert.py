# EC 500 Building Software
# Jacob Davis Assignment 1
# Spring 2020

# All digits can be represented separately and synthesized together per digit.
# Numerals needed to represent the 1's digit: I, V, and X
# Numerals needed to represent the 10's digit: X, L, and C
# Numerals needed to represent the 100's digit: C, D, and M
# Numerals needed to represent the 1000s digit: M, (V), (X)
# ...and so on

# Roman numeral representations
roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '(V)', '(X)', '(L)', '(C)', '(D)', '(M)']

def convert_to_rom(arabic_num):
    '''
    Converts input Arabic numeral into Roman numeral. Returns Roman numeral as a string.
    '''
    # Check whether the provided input can be represented
    if (arabic_num > 10**(len(roman_numerals) - 1)): 
        return "N/A" # Cannot represent numbers beyond the provided numerals
    elif (not isinstance(arabic_num, int)):         
        return "N/A" # Cannot represent non-integer values

    # Convert the number if it is an integer with a magnitude that is in range
    power_of_ten = 0  # Digit of focus
    roman_num = ""    # Output of function
    while (arabic_num > 0):
        digit = arabic_num % 10 # Get first digit
        digit_string = ""
        print(arabic_num)
        #The naming conventions of roman numerals for each digit, depending on power of 10
        if (digit == 1):   digit_string = roman_numerals[power_of_ten]
        elif (digit == 2): digit_string = roman_numerals[power_of_ten] * 2
        elif (digit == 3): digit_string = roman_numerals[power_of_ten] * 3 
        elif (digit == 4): digit_string = roman_numerals[power_of_ten] + roman_numerals[power_of_ten+1]
        elif (digit == 5): digit_string = roman_numerals[power_of_ten+1]
        elif (digit == 6): digit_string = roman_numerals[power_of_ten+1] + roman_numerals[power_of_ten]
        elif (digit == 7): digit_string = roman_numerals[power_of_ten+1] + (roman_numerals[power_of_ten] * 2)
        elif (digit == 8): digit_string = roman_numerals[power_of_ten+1] + (roman_numerals[power_of_ten] * 3)
        elif (digit == 9): digit_string = roman_numerals[power_of_ten] + roman_numerals[power_of_ten+2]
            
        # Place digit representation in front of entire number
        roman_num = digit_string + roman_num

        power_of_ten += 2                 # Increment a power of 10
        arabic_num = int(arabic_num / 10) # Move on to next digit

    return roman_num