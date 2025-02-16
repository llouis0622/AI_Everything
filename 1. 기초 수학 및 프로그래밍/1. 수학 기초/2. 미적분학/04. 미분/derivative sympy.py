from sympy import *

x = symbols('x')
f = x ** 2
dx_f = diff(f)
print(dx_f)
print(dx_f.subs(x, 2))