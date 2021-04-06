from helper_predicates import *
#import random
import time
import matplotlib.pyplot as plt

'''
def invariant_outer(values, old_values, i):
    return is_sorted(values[:i]) and \
           is_permutation(values, old_values)
'''
def insertion_sort(values):
   # old_values = values[:] # enkel voor invariant
    i = 0 # invariant waar, lege lijst is gesorteerd en permutatie is ook waar, want we hebben niets gewijzigd
    #assert invariant_outer(values, old_values, i)
    while i != len(values):
        #assert invariant_outer(values, old_values, i)
        j = i
        # zelf deze lusinvariant bedenken, geen idee of dit goed is
        #assert is_sorted(values[:j]) and is_sorted(values[j:i+1]) and is_permutation(values, old_values)
        while j > 0 and values[j-1] > values[j]:
            #assert is_sorted(values[:j]) and is_sorted(values[j:i + 1]) and is_permutation(values, old_values)
            values[j-1], values[j] = values[j], values[j-1]
            j -= 1
            #assert is_sorted(values[:j]) and is_sorted(values[j:i+1]) and is_permutation(values, old_values)
        #assert is_sorted(values[:j]) and is_sorted(values[j:i+1]) and is_permutation(values, old_values)
        i += 1
       # assert invariant_outer(values, old_values, i)
   # assert invariant_outer(values, old_values, i)


#Test
# Lijst op zelfde manier door elkaar gooien
#random.seed(123)
ns = list(range(0, 10000, 1000))
ts = []
#random.shuffle(lst)

ts_worst = []
for n in ns:
#print(lst)
    lst = list(range(n))

    start = time.perf_counter()
    insertion_sort(lst)
    end = time.perf_counter()
    #print(lst)
    ts.append(end-start)
    #ts_worst.append(end-start)

for n in ns:
#print(lst)
    lst = list(range(n, 0, -1))

    start = time.perf_counter()
    insertion_sort(lst)
    end = time.perf_counter()
    #print(lst)
    ts_worst.append(end-start)

plt.plot(ns, ts, 'bo-') #blauwe kleur met cirkels voor datapunten en lijn ertussen
plt.plot(ns, ts_worst, 'ro-')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.show() #min of meer lineair verloop voor best case en min of meer kwadratisch verloop voor worst-case
