# make sure the strings of all months have the same length
jan = "January   "
feb = "February  "
mar = "March     "
apr = "April     "
may = "May       "
jun = "June      "
jul = "July      "
aug = "August    "
sep = "September "
oco = "October   "
nov = "November  "
dec = "December  "

# length of a month
len_month = len(jan)

# concatenate all months to one very long string
all_months = jan + feb + mar + apr + may + jun + jul + aug + sep + oco + nov + dec

# the user starts counting the months at 1, therefore you need to subtract 1 to the given number
number = int(input("Please the number of the month: ")) - 1

# select the correct month
month = all_months[number*len_month : number*len_month + len_month]
print("The corresponding month is: " + month)