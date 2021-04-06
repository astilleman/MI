#
# Oefening 2
#
def abs(value):
    if value < 0:
        return -value
    else:
        return value


def gcd(a, b):
    modulo = a % b
    if modulo == 0:
        return b
    else:
        return gcd(b, modulo)

print(gcd(5, 24))


def gcd_nonrec(a, b):
    modulo = a % b
    while(modulo != 0):
        a, b = b, modulo
        modulo = a % b
    return b


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


assert abs(5) == 5
assert abs(-7) == 7
assert gcd(78, 66) == 6
assert lcm(3, 4) == 12
assert lcm(10, 4) == 20



#
# Oefening 3
#
# Dit is de originele (inefficiënte) Fibonacci-implementatie
def fibonacci(number):
    print(f" - bereken fibonacci({number})")
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def additive_sequence(number, t0, t1):
    print(f" - bereken additive_sequence({number}, {t0}, {t1})")
    if number == 0:
        return t0
    elif number == 1:
        return t1
    else:
        return additive_sequence(number - 1, t1, t0 + t1)


def fib_fast(number):
    return additive_sequence(number, 0, 1)


print("Inefficiënte berekening van Fibonacci(10) start")
f10 = fibonacci(10)
print("Resultaat:", f10)

print("Efficiënte berekening van Fibonacci(10) start")
f10 = fib_fast(10)
print("Resultaat:", f10)
