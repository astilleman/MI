"""
Write a program that computes the inner product of two vectors. The program first
asks the user the x- and y-coordinate of the first vector, and then the x- and
y-coordinate of the second vector.

Example output:
    Enter x-coordinate of the first vector: 2.2
    Enter y-coordinate of the first vector: 3.3
    Enter x-coordinate of the second vector: 2
    Enter y-coordinate of the second vector: 1
    Inner product is: 7.7
"""
'''
# Ask input from user
x_coo1 = float(input("Enter x-coordinate of the first vector: "))
y_coo1 = float(input("Enter y-coordinate of the first vector: "))
x_coo2 = float(input("Enter x-coordinate of the second vector: "))
y_coo2 = float(input("Enter y-coordinate of the second vector: "))

# Calculation inner product
inner_product = x_coo1 * x_coo2 + y_coo1 * y_coo2

# print result in the correct format
print("Inner product is:", inner_product)
'''

'''
2e versie met input validatie
'''

# Ask input from user
x_coo1 = input("Enter x-coordinate of the first vector: ")
y_coo1 = input("Enter y-coordinate of the first vector: ")
x_coo2 = input("Enter x-coordinate of the second vector: ")
y_coo2 = input("Enter y-coordinate of the second vector: ")
x_coo1_new = ""
y_coo1_new = ""
x_coo2_new = ""
y_coo2_new = ""

for i in x_coo1:
    if i != '.':
        x_coo1_new += i
for j in y_coo1:
    if j != '.':
        y_coo1_new += j
for k in x_coo2:
    if k != '.':
        x_coo2_new += k
for l in y_coo2:
    if l != '.':
        y_coo2_new += l

while (x_coo1 == "" or not (x_coo1_new.isdigit() or (x_coo1[0] == "-" and x_coo1[1].isdigit()))):
        x_coo1 = input("Enter x-coordinate of the first vector: ")
x_coo1 = float(x_coo1)
while (y_coo1 == "" or not (y_coo1_new.isdigit() or (y_coo1[0] == "-" and y_coo1[1].isdigit()))):
    y_coo1 = input("Enter y-coordinate of the first vector: ")
y_coo1 = float(y_coo1)
while (x_coo2 == "" or not (x_coo2_new.isdigit() or (x_coo2[0] == "-" and x_coo2[1].isdigit()))):
    x_coo2 = input("Enter x-coordinate of the second vector: ")
x_coo2 = float(x_coo2)
while (y_coo2 == "" or not (y_coo2_new.isdigit() or (y_coo2[0] == "-" and y_coo2[1].isdigit()))):
    y_coo1 = input("Enter y-coordinate of the second vector: ")
y_coo2 = float(y_coo2)

# Calculation inner product
inner_product = x_coo1 * x_coo2 + y_coo1 * y_coo2


# print result in the correct format
print("Inner product is:", inner_product)
