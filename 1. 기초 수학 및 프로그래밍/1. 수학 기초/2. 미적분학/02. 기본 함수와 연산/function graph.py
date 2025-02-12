from sympy import *
from sympy.plotting import plot3d

x1 = symbols('x')
f1 = 2 * x1 + 1
plot(f1)

x2 = symbols('x')
f2 = x2 ** 2 + 1
plot(f2)

x3, y3 = symbols('x y')
f3 = 2 * x3 + 3 * y3
plot(f3)