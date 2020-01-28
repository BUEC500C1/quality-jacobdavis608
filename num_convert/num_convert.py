# EC 500 Building Software
# Jacob Davis Assignment 1
# Spring 2020
import sys

def convert_to_rom(arabic_nums):
    '''
    Converts input Arabic numerals into Roman numerals. Returns a list 
    of strings representing the Roman numerals.
    '''
    # Convert all arabic nums
    for num in arabic_nums:
        print(num)



    return arabic_nums
    

def main():
    # Check the command line for arguments
    if (len(sys.argv) <= 1):
        print("No arguments provided\n")
    else: #pass arguments to conversion
        roman_numerals = convert_to_rom(sys.argv[1:])

if __name__ == "__main__":
    main()