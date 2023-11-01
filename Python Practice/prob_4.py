import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2*x*x*x + 9*x**2 + 7*x -6
def df(x):
    return 6*x**2 + 18*x + 7

x0 = 0.51
tol = 1e-6
x = x0
xNext = 0
counter = 0

for i in range(0, 50):
    xNext = x - (f(x)/df(x))
    print(xNext)
    print("The number of iterations is:", i)
