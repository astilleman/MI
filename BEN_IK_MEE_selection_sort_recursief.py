from helper_predicates import *
import random

def selection_sort(values, i):  # enkel voor invariant
    if i <= 0:
        return
    else:
        maxPos = values.index(max(values[:i+1]))
        values[i], values[maxPos] = values[maxPos], values[i]  # Korte manier om te schrijven dat 2 elementen van plaats veranderen
        # temp = values[i]
        # values[i] = values[minPos]
        # values[minPos] = temp # Dit is langere versie
        selection_sort(values, i-1)


#Test
# Lijst op zelfde manier door elkaar gooien
random.seed(123)

lst = list(range(20))
random.shuffle(lst)

print(lst)
selection_sort(lst, 19)
print(lst)