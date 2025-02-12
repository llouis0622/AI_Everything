from math import exp

p1 = 100
r1 = 0.2
t1 = 2.0
n1 = 12
a1 = p1 * (1 + (r1 / n1)) ** (n1 * t1)
print(a1)

p2 = 100
r2 = 0.2
t2 = 2.0
a2 = p2 * exp(r2 * t2)
print(a2)