###############PART 1
def one(value):
    value = 20
    two(value)
    # 3: Python geeft voorrang aan lokale variabelen dus 20 wordt geprint
    print(value)

def two(v):
    # 2: v krijgt waarde 20 mee, maar value wordt afgedrukt dus 10
    print(value)
    three()

def three():
    # Deze functie doet niets
    value = 20
    four()

def four():
    # Deze functie maakt van value een globale variabele dus value veranderd in 110
    global value
    value = value + 100

value = 10
# 1: value 10 wordt afgedrukt
print(value)
one(value*3)
# 4: De globale variabele 110 wordt geprint
print(value)

############PART 2
# 1) gcd (greatest common divisor)
# while-loop
def greatest_common_divisor(number1, number2):
    value1 = max(number1, number2)
    value2 = min(number1, number2)
    while value1 % value2 != 0:
        old_value2 = value2
        value2 = value1 % value2
        value1 = old_value2
    return value2


print(greatest_common_divisor(48, 36))
# recursief
def greatest_common_divisor_rec(number1, number2):
    value1 = max(number1, number2)
    value2 = min(number1, number2)
    return greatest_common_divisor(value2, value1 % value2)

print(greatest_common_divisor_rec(36, 48))
# 2) absolute value
def absolute_value(number):
    if number < 0:
        return -number
    else:
        return number

print(absolute_value(-5))
print(absolute_value(0))
print(absolute_value(5))
# 3) lcm (lowest common multiplier)
def lowest_common_multiplier(number1, number2):
    # Zonder int geeft hij 36.0 weer in mijn geval
    return int(absolute_value(number1 * number2)/greatest_common_divisor(number1, number2))

print(lowest_common_multiplier(4, 18))

#########PART 3
def fibonacci(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return fibonacci_numbers[n - 1]

print(fibonacci(10))




