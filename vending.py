## BOEK
# This program simulates a vending machine that gives change.
#

#Define constants.
PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25

# Obtain input from user. (2e ook int, want in pennies)
userInput = input("Enter bill value (1 = $1 bill, 5 = $5 bill, etc.): ")
billValue = int(userInput)
userInput = input("Enter price in pennies: ")
ItemPrice = int(userInput)

# Compute change due.
changeDue = PENNIES_PER_DOLLAR * billValue - ItemPrice
dollarCoins = changeDue // PENNIES_PER_DOLLAR
changeDue = changeDue % PENNIES_PER_DOLLAR
quarters = changeDue // PENNIES_PER_QUARTER

# Print change due.
print("Dollar coins:  %6d" % dollarCoins)
print("Quarters:      %6d" % quarters)
