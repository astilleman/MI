'''
sentence = input("Geef een zin in: ")

for i in range(len(sentence)):  # Gebruik indices omdat je alle chars wilt printen, maar toch alterneren!
    if i % 2 == 0:
        print(sentence[i].upper(), end="")
    else:
        print(sentence[i], end="")
'''
import math
print(math.trunc(5.6))
print(math.cos(math.pi/3))
lijst = [1, 4, 6, 7, 6, 9, 10]
n = lijst.remove(4)
print(lijst)
print(n)
t = (1, 2, 2)
s = 7,
print(s)
print(t + s)
k = (7,)

print(t + k)