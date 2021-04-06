from helper_predicates import *
import random
import time
import matplotlib.pyplot as plt

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
print(lst)

# PLOT
ns = list(range(0, 1000, 100))
ts = []

for n in ns:
    lst = list(range(n))
    random.shuffle(lst)
    start = time.perf_counter()
    selection_sort(lst)
    end = time.perf_counter()
    ts.append(end-start)
    print(n, end-start)

plt.plot(ns, ts, 'bo-') #blauwe kleur met cirkels voor datapunten en lijn ertussen
plt.xlabel('n')
plt.ylabel('T(n)')
plt.show()