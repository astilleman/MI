"""
Schrijf met behulp van een while lus een programma dat het kleinst gemeenschappelijke veelvoud van twee getallen berekent.
Bewijs de correctheid.
"""
a = 10
b = 15

def gcd(a, b):
    modulo = a % b
    if modulo == 0:
        return b
    else:
        return gcd(b, modulo)

def absolute_value(number):
    if number < 0:
        return -number
    else:
        return number
def lowest_common_multiplier(number1, number2):
    # Zonder int geeft hij 36.0 weer in mijn geval
    return int(absolute_value(number1 * number2)/gcd(number1, number2))

assert True
lcm = lowest_common_multiplier(a, b)
assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) #3.OK
while a != b:
    oude_variant = abs(a-b) #1. oude_variant == V
    assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) and a != b and abs(a-b) == oude_variant #1. I and E and V == oude_variant
    if a > b:
        assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) and a != b and abs(a-b) == oude_variant and a > b #1. I and E and V == oude_variant and E1
        assert 0 <= a-b and 0 <= b and lcm == lowest_common_multiplier(a-b, b) and 0 <= abs(a-2*b) < oude_variant # 2. propgareer naar boven
        #3.OK 0 <= a and 0 <= b and a > b => 0 <= a-b and 0 <= b en
        a = a - b
        assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) and 0 <= abs(a-b) < oude_variant #1. I and 0 <= V < oude_variant
    else:
        assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) and a != b and abs(a-b) == oude_variant and not a > b #I and E and V == oude_variant and not E1
        assert 0 <= a and 0 <= b-a and lcm == lowest_common_multiplier(a, b-a) and 0 <= abs(2*a-b) < oude_variant#2 propageer naar boven
        #3.OK
        b = b - a
        assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) and 0 <= abs(a-b) < oude_variant # 2. propageer naar boven
    assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) and 0 <= abs(a-b) < oude_variant #1. I and 0 <= V < oude_variant
assert 0 <= a and 0 <= b and lcm == lowest_common_multiplier(a, b) and not a != b #1. I and not E

print("De grootste gemeenschappelijke deler is", a)