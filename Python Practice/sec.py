import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative


def f(x):
    return x**3 - 5*x - 6


def df(x):
    return 3*x**2 - 5


# Secant method
x1 = 1
x2 = 3
tol = 1e-5
error = abs(x2 - x1)
n = 0

max_iteration = 20
x3 = 5

Iterations = []


def graph(x2, x3, n):
    errors = []
    Iterations = []

    for n in range(1, max_iteration):
        x3 = (x1*f(x2) - x2*f(x1))/(f(x2) - f(x1))
        if f(x1)*f(x3) < 0:
            x2 = x3
            error = abs(x1 - x3)
            errors.append(error)
        if f(x2)*f(x3) < 0:
            x1 = x3
            error = abs(x2 - x3)
            errors.append(error)

    n = n + 1
    Iterations.append(n)
    return Iterations, errors


graph_n, graph_error = graph(x2, x3, n)


print(f"Error in {n} iteration is {error}")
print(f"No of iterations {n}")


print(f"value {x3}")
plt.plot(graph_n, graph_error)
