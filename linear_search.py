from helper_predicates import *
import random

def linear_search(values, target):
    i = 0
    assert all(values[k] != target for k in range(0, i)) # alle elementen tot dan toe overlopen (van 0 tot i-1) zijn verschillend van target
    while i != len(values):
        assert all(values[k] != target for k in range(0, i))
        if values[i] == target:
            assert all(values[k] != target for k in range(0, i)) # lusinvariant hier ook, want return in lus betekent einde van lus,
            # invariant moet dus ook hier gelden, net voor we uit lus gaan en onze waarde teruggeven
            return i
        i += 1
        assert all(values[k] != target for k in range(0, i))
    assert all(values[k] != target for k in range(0, i))
    return -1




#Test
# Lijst op zelfde manier door elkaar gooien
random.seed(123)

lst = list(range(20))
random.shuffle(lst)

print(lst)
print(linear_search(lst, 12))
print(linear_search(lst, 50))