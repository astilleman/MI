"""
Write a program that reads a five-digit positive integer and breaks into a sequence of individual
digits, with each digit on a new line

Example:
    Please enter a 5-digit number: 12345
    The result is:
    1
    2
    3
    4
    5

Hint: use the \n escape sequence that denotes a "newline" character, that causes subsequent characters
to be printed on a new line
"""

# Ask input from user
number = input("Please give a 5 digit number: ")

# Print result
print("The result is:\n%s\n%s\n%s\n%s\n%s" % (number[0], number[1], number[2], number[3], number[4]))