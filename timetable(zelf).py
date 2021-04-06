# Ask input from user
seconds = int(input('Give number of seconds: '))

# Calculation of hours, minutes and seconds
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

#Print
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
