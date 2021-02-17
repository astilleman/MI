"""
Write a program that can transform numbers 1,2,3,...,12 into the corresponding month names January,
February, March, ..., December. The program asks the user for a number, and prints the correct month.
Notice that January is month number 1. Also notice that this exercise can be solved using if-else-
statements, however, try not using these statements to solve this exercise.

Example:
    Please enter the number of the month: 8
    The corresponding month is: August

Hint: Make a very long string "January February March ... December" in which you add spaces
such that each month has the same length. Then select the characters of the month that you want.
Extra hint: The longest month has 9 characters

Hint: Use the : operator for strings
"""

# Ask input from user
month_number = int(input("Please enter the number of the month: "))

# Conversion from number to corresponding month
# For each month we have 9 characters
month_string = "Januari  Februari Maart    April    Mei      Juni     Juli     Augustus SeptemberOktober  November December "

# Print result
# pseudocode: januari ~ 0-9, februari ~ 9-18, maart ~ 18-27, ...
# function .strip() removes all blank spaces
print("Name of month:", (month_string[9 * (month_number - 1): 9 * month_number]).strip())