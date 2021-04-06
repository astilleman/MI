from helper_predicates import *
import random

def quick_sort(values, start, to): # we beschouwen to inbegrepen
    if start >= to: # basisgeval bij recursie, geen of 1 element om te sorteren dus uit functie zonder iets te doen
        return
    p = partition(values, start, to)
    quick_sort(values, start, p-1)
    quick_sort(values, p+1, to) # pivot zelf hoeven we zelf niet mee te nemen, want die staat na het partitioneren op de juiste plaats

def invar(values, start, i, pivot, geq):
    return values[start] == pivot and \
           all(values[k] < pivot for k in range(start+1, geq)) and \
           all(values[k] >= pivot for k in range(geq, i))


def partition(values, start, to):
    pivot = values[start]
    i = start+1
    geq = start+1 # op 2 plaatsen lege range in invar dus sws voldaan
    assert invar(values, start, i, pivot, geq)
    while i != to + 1:
        assert invar(values, start, i, pivot, geq)
        if values[i] >= pivot:
            pass
        else:
            values[i], values[geq] = values[geq], values[i]
            geq += 1
        i += 1
        assert invar(values, start, i, pivot, geq)
    assert invar(values, start, i, pivot, geq)
    geq -= 1 # we komen op laatste element dat strikt kleiner is dan pivot
    values[geq], values[start] = values[start], values[geq]
    return geq

print(partition([4, 15, 5, 3, 5, 11, 8, 12, 19], 0, 8))

#Test
# Lijst op zelfde manier door elkaar gooien
random.seed(123)

lst = list(range(20))
random.shuffle(lst)

print(lst)
quick_sort(lst, 0, len(lst)-1) # start en to in testprogramma invoeren
print(lst)