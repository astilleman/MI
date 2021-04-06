number = input("Please enter a number between 1000 and 999999: ")

# this index decides where the comma will be placed
# len(number) is the last letter of the string
# len(number) -3 is the third letter counting from left
split_index = len(number) - 3

formatted_number = number[: split_index] + "," + number[split_index:]

## alternative solution
formatted_number2 = number[:-3] + "," + number[-3:]
print("The formatted number is: " + formatted_number)
print("The formatted number 2 is: " + formatted_number2)
