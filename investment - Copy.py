##
#  This program prints a table showing the growth of an investment.
#
'''
# Define constant variables.
RATE = 5.0
INITIAL_BALANCE = 10000.0

# Obtain the number of years for the computation.
numYears = int(input("Enter number of years: "))
   
# Print the table of balances for each year.
balance = INITIAL_BALANCE
for year in range(1, numYears + 1) :
   interest = balance * RATE / 100
   balance = balance + interest
   print("%4d %10.2f" % (year, balance))

'''
# Define constant variables.
RATE = 5.0
INITIAL_BALANCE = 10000.0

# Obtain the number of years for the computation.
numYears = int(input("Enter number of years: "))

# Print the table of balances for each year.
balance2 = INITIAL_BALANCE
count = 1
while count <= numYears:
   interest = balance2 * RATE / 100
   balance2 = balance2 + interest
   print("%4d %10.2f" % (count, balance2))
   count += 1
