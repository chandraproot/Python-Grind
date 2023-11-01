import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative


def f(x):
    return x**3 - 5*x - 6


def df(x):
    return 3*x**2 - 5

# Newton-Raphson method


def newton_raphson(x0, tol, max_iter):
    x = x0
    errors = []

    for k in range(max_iter):
        x = x - f(x) / df(x)
        error = abs(x - (2.6890953236376594))  # True root is -2
        errors.append(error)

        if error < tol:
            break

    return x, errors


# Initial guess and tolerance
x0 = 2
tolerance = 1e-6
max_iterations = 50

# Calculate the root and errors using the Newton-Raphson method
newton_root, newton_errors = newton_raphson(x0, tolerance, max_iterations)

# Plot the errors
plt.figure(figsize=(9, 5))
plt.plot(newton_errors)
plt.xlabel("Number of Iterations")
plt.ylabel("Error")
plt.title("Newton-Raphson Method Error Convergence")
plt.grid()
plt.show()

print(f"Newton-Raphson root: {newton_root}")
