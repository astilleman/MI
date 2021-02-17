"""
Write a program that reads a number of seconds and then converts this to the number of  days, hours,
minutes and seconds and prints this to the user. Notice that this exercise can be solved using if-else-
statements, however, try not to use these statements to solve this exercise.

Example:
    Time in seconds: 86491
    1 days, 0 hours, 1 minutes, 31 seconds

Hint: you will need the integer division (//) and modulo operator (%)
"""

# Ask input from user
amount_of_seconds = int(input("Enter an amount of seconds: "))

# Calculation of hours, minutes and seconds
amount_of_days = amount_of_seconds // (3600 * 24)
amount_of_seconds = amount_of_seconds % (3600 * 24)
amount_of_hours = amount_of_seconds // 3600
amount_of_seconds = amount_of_seconds % 3600
amount_of_minutes = amount_of_seconds // 60
amount_of_seconds = amount_of_seconds % 60

# Print result in the correct format
print("%d days, %d hours, %d minutes, %d seconds" %(amount_of_days, amount_of_hours, amount_of_minutes, amount_of_seconds))
