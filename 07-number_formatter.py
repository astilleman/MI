"""
Write a program that reads an integer between 1000 and 999999 from the user, and prints
it with a comma separating the thousands:

Example:
    Please enter an integer between 1000 and 999999: 23456
    The formatted number is: 23,456

Hint: use the : operator for strings
"""

# Ask input from user
number = input("Please enter a number between 1000 and 999999: ")

# Calculations
part_after_comma = int(number[len(number)-3: len(number)])
part_before_comma = (int(number) - part_after_comma) / 1000

# Print result
print("The formatted number is: %d,%d" % (part_before_comma, part_after_comma))
