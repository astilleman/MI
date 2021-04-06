from helper_predicates import *
import random

# Omdat we dit recursief oproepen en weten dat we bij binary_search naar deel van lijst willen kijken,
# gaat het nodig zijn om extra parameters te introduceren
# start en end (exclusief) / end is 1 ste index na het laatste element
def binary_search(values, target, start, end):
    if start >= end: #lege lijst dan zeker dat element niet vookomt #BASECASE
        return -1
    mid = (start+end)//2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        # mid zelf niet meer beschouwen, want sws verschillend van target
        return binary_search(values, target, mid+1, end)
    else: #values[mid] > target
        # hier niet mid-1 schrijven, want end was exclusief
        return binary_search(values, target, start, mid)



#Test
# Enkel op gesorteerde lijst!
lst = list(range(20))

print(lst)
print(binary_search(lst, 12, 0, len(lst))) # testcode ook aanpassen
print(binary_search(lst, 50, 0, len(lst)))
