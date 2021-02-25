### MAGIC SQUARE

# Ask input from user
values = []
for i in range(16):
    values.append(int(input("Give a number: ")))

# Initialisation
row_sum = 0
column_sum = 0
diagonal_sum1 = 0
diagonal_sum2 = 0
row_sum_list = []
column_sum_list = []
one_to_sixteen = False


# Table
table = []
for i in range(4):
    empty_list = []
    for j in range(4):
        empty_list.append(values[i*4 + j])
    table.append(empty_list)


# Part1: testing of each number from 1 to 16 (both included) occurs
i = 0
values_check = []
while i < 16 and values[i] not in values_check and 1 <= values[i] <= 16:
    values_check.append(values[i])
    i += 1

if values == values_check:
    one_to_sixteen = True

# Part2: row_sum == column_sum == diagonal1_sum == diagonal2_sum ?
# Calculating row_sum, column_sum, diagonal1_sum and diagonal2_sum
for i in range(4):
    for j in range(4):
        row_sum += table[i][j]
        column_sum += table[j][i]
        if i == j:
            diagonal_sum1 += table[i][j]
        elif i == 3 - j:
            diagonal_sum2 += table[i][j]
    row_sum_list.append(row_sum)
    column_sum_list.append(column_sum)
    row_sum, column_sum = 0, 0
# Checking if the sums matches:
check_list1 = []
for number in row_sum_list:
    check_list1.append(number)
for number in column_sum_list:
    check_list1.append(number)
check_list1.append(diagonal_sum1)
check_list1.append(diagonal_sum2)
check_list2 = []
same = True
i = 1

check_list2.append(check_list1[0])
while i < (len(check_list1)) and same:
    check_list2.append(check_list1[i])
    if check_list1[i-1] != check_list1[i]:
        same = False
    i += 1
if check_list1 == check_list2 and one_to_sixteen:
    print("This is a magic square with magic sum", check_list1[0])
else:
    print("This is no magic square :(")



print(check_list1)
print(check_list2)
print(diagonal_sum1)
print(diagonal_sum2)
print(row_sum_list)
print(column_sum_list)




#print(values)
print(table)
stringvalues = ""
for i in range(len(values)):
    stringvalues += str(values[i]) + " "
print(stringvalues)
print(one_to_sixteen)