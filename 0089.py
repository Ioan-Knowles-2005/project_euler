# Roman Numerals
# For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
# Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of
# writing a particular number.

#For example, it would appear that there are at least six ways of writing the number sixteen:

# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI

#However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most 
# efficient, as it uses the least number of numerals.
#Find the number of characters saved by writing each of these in their minimal form.

def roman_to_int(roman):
    """Convert a Roman numeral to an integer."""
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(roman):  # Process from right to left
        value = roman_values[char]
        if value < prev_value:
            total -= value  # Subtractive notation (e.g., IV = 4, IX = 9)
        else:
            total += value
        prev_value = value

    return total

def int_to_roman(num):
    """Convert an integer to its minimal Roman numeral representation."""
    int_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman = ""
    for value, symbol in int_to_roman_map:
        while num >= value:
            roman += symbol
            num -= value

    return roman

def count_characters_saved(filename):
    """Compute the number of characters saved by converting to minimal form."""
    with open(filename, 'r') as file:
        roman_numerals = file.read().splitlines()

    total_saved = 0

    for numeral in roman_numerals:
        original_length = len(numeral)
        minimal_length = len(int_to_roman(roman_to_int(numeral)))
        total_saved += (original_length - minimal_length)

    return total_saved

filename = "problem_89_roman.txt"  
characters_saved = count_characters_saved(filename)
print("Total characters saved:", characters_saved)