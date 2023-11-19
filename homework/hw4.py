import math
from numpy import arange
def equation(x):
    return x**2 - 3*x + 1

for i in arange(-100, 100,0.001):
    fx = equation(i)
    if abs(equation(i)) < 0.001:
        print(f"x = {i}, f(x) = {fx}")
