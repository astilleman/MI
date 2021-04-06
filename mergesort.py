from helper_predicates import *
import random

def merge_sort(values):
    # recursieve functie dus basisgeval nodig
    if len(values) <= 1:
        return
    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_lists(left, right, values)

def merge_lists(first, second, values):
    assert is_sorted(first)
    assert is_sorted(second)

    k = 0 # volgende index in values
    i1 = 0 # volgend element uit first
    i2 = 0 # volgend element uit second
    assert is_permutation(values[:k], first[:i1] + second[:i2]) and is_sorted(values[:k])
    while k != len(values):
        assert is_permutation(values[:k], first[:i1] + second[:i2]) and is_sorted(values[:k])
        first_available = i1 < len(first)
        second_available = i2 < len(second)
        if not second_available or (first_available and first[i1] <= second[i2]):
            values[k] = first[i1]
            i1 += 1
        else:
            values[k] = second[i2]
            i2 += 1
        k += 1
        assert is_permutation(values[:k], first[:i1] + second[:i2]) and is_sorted(values[:k])
    assert is_permutation(values[:k], first[:i1] + second[:i2]) and is_sorted(values[:k])


#Test
# Lijst op zelfde manier door elkaar gooien
random.seed(123)

lst = list(range(20))
random.shuffle(lst)

print(lst)
merge_sort(lst)
print(lst)