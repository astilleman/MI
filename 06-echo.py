"""
Write a program that echoes a given input a number of given times

Example:
    What do you want to be echoed? echo
    How many times do you want it to be echoed? 6
    echo echo echo echo echo echo

Notice that in this example the user input was: "echo "
"""
# Ask input from user
text = input("What do you want to be echoed? ")
count = int(input("How many times do you want it to be echoed? "))

# Print result
print(text * count)