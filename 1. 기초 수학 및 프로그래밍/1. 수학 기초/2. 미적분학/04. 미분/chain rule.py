from sympy import *

x = symbols('x')
z = (x ** 2 + 1) ** 3 - 2
dz_dx = diff(z, x)
print(dz_dx)