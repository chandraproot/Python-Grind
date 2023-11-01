import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^3 - 5x - 6


def f(x):
    return x**3 - 5*x - 6


# Define the initial guesses
x0 = 1.0
x1 = 3.0

# Define the tolerance for convergence
tolerance = 1e-6

# Initialize lists to store values
x_values = [x0, x1]
error_values = []

# Set a maximum number of iterations
max_iterations = 50

# Perform the secant method
for k in range(2, max_iterations + 2):
    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    error = abs(x2 - x_values[-1])
    x_values.append(x2)
    error_values.append(error)

    if error < tolerance:
        break

    # Update x0 and x1 for the next iteration
    x0 = x1
    x1 = x2

# Plot the error as a function of iterations
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(error_values) + 1),
         error_values, marker='o', linestyle='-')
plt.xlabel('Iteration (k)')
plt.ylabel('Absolute Error (ϵ_k)')
plt.title('Convergence of Secant Method')
plt.grid(True)
plt.show()

# Print the root approximation
print(f"Approximate root (x_r): {x_values[-1]}")
