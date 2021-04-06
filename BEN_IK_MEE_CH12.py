import time
import matplotlib.pyplot as plt

def binary_search(values, target):
    if len(values) == 0:
        return -1
    mid = len(values) // 2
    left = values[:mid]
    right = values[mid+1:]
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        result = binary_search(right, target)
        if result > -1:
            return mid + 1 + result
        return -1
    else:
        return binary_search(left, target)

# PLOT
ns = list(range(0, 1000, 100))
ts = []
ts_worst = []

for n in ns:
    lst = list(range(n))
    start = time.perf_counter()
    binary_search(lst, (n-1)//2)
    end = time.perf_counter()
    ts.append(end-start)

for n in ns:
    lst = list(range(n))
    start = time.perf_counter()
    binary_search(lst, 0)
    end = time.perf_counter()
    ts_worst.append(end-start)

plt.plot(ns, ts, 'bo-') #blauwe kleur met cirkels voor datapunten en lijn ertussen
plt.plot(ns, ts_worst, 'ro-')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.show()