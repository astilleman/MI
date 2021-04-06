"""
Schrijf met behulp van een while lus een programma dat het n-de fibonacci getal berekent.
Bewijs de correctheid.
"""

def fibonacci(n):
    first = 1
    second = 1

    if n == 0:
        return first
    if n == 1:
        return second
    else:
        min_2 = first
        min_1 = second
        i = 2
        while i < n + 1:
            fib = min_2 + min_1
            min_2 = min_1
            min_1 = fib
            i += 1
        return fib


x= 1
y = 1
n = 13
hulp = 1


assert 0 < n #1. P
i = 0 #3. OK
assert 0 <= i <= n and x == fibonacci(i) and 0 <= x and 0 <= y and 0 <= hulp  # 1.I
while i < n:
    oude_variant = n - i
    assert 0 <= i <= n  and x == fibonacci(i) and 0 <= x and 0 <= y and 0 <= hulp and i < n and  n - i == oude_variant # 1. I and E and V == oude_variant
    assert 0 <= i + 1 <= n and y == fibonacci(i + 1) and 0 <= x and 0 <= x+y and 0 <= x and 0 <= n-(i+1) < oude_variant #2. propageer naar boven
    #3. OK, 0 <= i <= n and  i < n => 0 <= i + 1 <= n en x == fibonacci(i)  and  0 <= y => y == fibonacci(i + 1) and 0 <= x+y, omdat y 1
    #plaats verder staat in fibonacci reeks dan x
    hulp = x
    assert 0 <= i + 1 <= n and y == fibonacci(i + 1) and 0 <= y and 0 <= hulp+y and 0 <= hulp and 0 <= n-(i+1) < oude_variant #2. propageer naar boven
    x = y
    assert 0 <= i + 1 <= n and x == fibonacci(i + 1) and 0 <= x and 0 <= hulp+y and 0 <= hulp and 0 <= n-(i+1) < oude_variant #2. propageer naar boven
    y = hulp + y
    assert 0 <= i+1 <= n and x == fibonacci(i+1) and 0 <= x and 0 <= y and 0 <= hulp and 0 <= n-(i+1) < oude_variant #2. propageer naar boven
    i += 1
    assert 0 <= i <= n and x == fibonacci(i) and 0 <= x and 0 <= y and 0 <= hulp and 0 <= n-i < oude_variant #1. I and 0<= V < oude_variant
assert 0 <= i <= n and x == fibonacci(i) and 0 <= x and 0 <= y and 0 <= hulp and not i < n #1. I and not E
assert x == fibonacci(n) #1.Q
