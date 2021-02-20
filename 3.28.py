# Ask input from user
number = int(input("Enter a number: "))

# Initialisation
roman_number = ""

# Defining thousands, hundreds, tens and ones
thousands = number // 1000
number = number % 1000
hundreds = number // 100
number = number % 100
tens = number // 10
number = number % 10
ones = number

# Roman number conversion
if number < 4000:
    # Thousands
    roman_number += thousands * "M"
    # Hundreds
    if hundreds == 9:
        roman_number += "CM"
    elif 5 <= hundreds <= 8:
        roman_number += "D" + (hundreds - 5) * "C"
    elif hundreds == 4:
        roman_number += "CD"
    elif 0 <= hundreds <= 3:
        roman_number += hundreds * "C"
    # Tens
    if tens == 9:
        roman_number += "XC"
    elif 5 <= tens <= 8:
        roman_number += "L" + (tens - 5) * "X"
    elif tens == 4:
        roman_number += "XL"
    elif 0 <= tens <= 3:
        roman_number += tens * "X"
    # Ones
    if ones == 9:
        roman_number += "IX"
    elif 5 <= ones <= 8:
        roman_number += "V" + (ones - 5) * "I"
    elif ones == 4:
        roman_number += "IV"
    elif 0 <= ones <= 3:
        roman_number += ones * "I"

# Print result
print(roman_number)