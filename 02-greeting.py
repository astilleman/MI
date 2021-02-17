"""
Write a program that asks a user for its first name and its surname, then
greets the user accordingly

Example:
    Enter your first name: John John
    Enter your last name: Florence
    Welcome John John Florence!
"""
# Ask input from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# print result
print("Welcome %s %s!" % (first_name, last_name))