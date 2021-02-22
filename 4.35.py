## CREDIT CARD NUMBER CHECK

# Ask input from user
credit_card_number = int(input("Enter a credit card number: "))

# Initialisation
credit_card_number_string = str(credit_card_number)
sum1 = 0
sum2_string = ""
sum2 = 0
valid = False
last_number = 0

# sum1
for i in range(4):
    sum1 += int(credit_card_number_string[7 - 2*i])

# sum2
for i in range(4):
    sum2_string += str(2*int(credit_card_number_string[6 - 2*i]))
for digit in sum2_string:
    sum2 += int(digit)

# sum3 = sum1 + sum2
sum3 = sum1 + sum2
last_number = int(str(sum3)[-1])
if last_number == 0:
    valid = True


# Print result
print(sum1)
print(sum2_string)
print(sum2)
if valid:
    print("The credit card number is valid.")
else:
    # sum1 has to change because the last digit is included in that sum
    if last_number > int(credit_card_number_string[-1]):
        difference = 10 - last_number
        check_number = int(credit_card_number_string[-1]) + difference
    else:
        check_number = int(credit_card_number_string[-1]) - last_number
    print("The credit card number is invalid. The check number should be", check_number)





