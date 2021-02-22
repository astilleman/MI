##
#  Check a credit card number to see if it is valid.
#

cc_num = input("Enter an 8 digit credit card number: ")

# Compute the sum of the digits at odd indices.
sum_odd = 0
for i in range(7, 0, -2) :
   sum_odd = sum_odd + int(cc_num[i])

# Compute the sum of the digits of the doubles of the digits at even indices.
sum_even = 0
for i in range(6, -1, -2) :
   double = int(cc_num[i]) * 2
   sum_even = sum_even + double // 10 + double % 10

# Compute the total of the sums from the odd digits and the even digits.
total = sum_odd + sum_even

# Display whether or not the credit card number was valid.
if total % 10 == 0 :
   print("That number is valid.")
else :
   # Compute what the check digit should be.
   check_digit = int(cc_num[7])
   should_be = (10 - (total % 10) + check_digit) % 10
   print("The number is not valid.  The check digit should be: ", should_be)

