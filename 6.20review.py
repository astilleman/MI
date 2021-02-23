# Run
number_list = [1, 2, 5, 5, 3, 1, 2, 4, 3, 2, 2, 2, 2, 3, 6, 5, 5, 6, 3, 1]

# Initialisation
length_list = []
length = 0

# While-loop
i = 0
while i < (len(number_list) - 1):
    value1 = number_list[i]
    value2 = number_list[i + 1]
    if value1 == value2:
        length += 1
        i += 1
    length_list.append(length)
    i += 1

# Print result
print(max(length_list))





