def roman_to_int(roman):
    total = 0

    # Translate 4s and 9s
    roman = roman.replace("IV", "IIII")
    roman = roman.replace("IX", "VIIII")
    roman = roman.replace("XL", "XXXX")
    roman = roman.replace("XC", "LCCCC")
    roman = roman.replace("CD", "CCCC")
    roman = roman.replace("CM", "DCCCC")

    # Set up the values for use
    trans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for digit in roman:
        total += trans[digit]

    return total

test = "MCMLXXXII"

print(roman_to_int(test))