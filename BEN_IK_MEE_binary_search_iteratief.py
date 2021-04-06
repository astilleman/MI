from helper_predicates import *
import random
'''
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
'''
'''
from helper_predicates import *
import random

def selection_sort_invariant(values, orig_values, i):
    return is_sorted(values[:i]) and \
           is_permutation(values, orig_values) and \
           all_lte_all(values[:i], values[i:])

def selection_sort(values):
    # Lus moet invariant hebben die 3 dingen zegt
    orig_values = values[:] # enkel voor invariant
    i = 0 # lusinvaiant is dan waar
    assert selection_sort_invariant(values, orig_values, i)
    while i != len(values):
        assert selection_sort_invariant(values, orig_values, i)
        minPos = minimum_position(values, i)
        values[i], values[minPos]= values[minPos], values[i] # Korte manier om te schrijven dat 2 elementen van plaats veranderen
        #temp = values[i]
        #values[i] = values[minPos]
        #values[minPos] = temp # Dit is langere versie
        i += 1
        assert selection_sort_invariant(values, orig_values, i)
    assert selection_sort_invariant(values, orig_values, i)

def minimum_position(values, start):
    minPos = start
    i = start + 1
    assert lte_all(values[minPos], values[start:i])
    while i != len(values):
        assert lte_all(values[minPos], values[start:i])
        if values[i] < values[minPos]:
            minPos = i
        i += 1
        assert lte_all(values[minPos], values[start:i])
    assert lte_all(values[minPos], values[start:i])
    return minPos


#Test
# Lijst op zelfde manier door elkaar gooien
random.seed(123)

lst = list(range(20))
random.shuffle(lst)

print(lst)
selection_sort(lst)
print(lst)'''



def binary_search(values, target):
    i = 0  # lusinvaiant is dan waar
    while values[i] != target and target <= len(values):
        midden = len(values) // 2
        eerste_helft = values[:midden]
        tweede_helft = values[midden:]
        if target in eerste_helft:
            midden = len(eerste_helft) // 2
            eerste_helft = values[:midden]
            tweede_helft = values[midden:]
        else:
            midden = len(tweede_helft) // 2
            eerste_helft = values[:midden]
            tweede_helft = values[midden:]
        i += 1
    if values[i] == target:
        return i
    else:
        return -1

#Test
# Enkel op gesorteerde lijst!
lst = list(range(20))

print(lst)
print(binary_search(lst, 12)) # testcode ook aanpassen
print(binary_search(lst, 50))
