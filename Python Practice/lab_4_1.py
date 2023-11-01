import numpy as np
import matplotlib.pyplot as plt

# Define the system of first-order ODEs
def f(x, y, z):
    dydx = z
    dzdx = -np.pi**2 * y - z
    return dydx, dzdx

# Parameters
x0 = 0  # Initial value of x
y0 = 1  # Initial value of y
z0 = 0  # Initial value of z (dy/dx)
h = 0.01  # Step size
x_end = 10  # End value of x

# Create arrays to store x, y, and z (dy/dx) values
x_values = [x0]
y_values = [y0]
z_values = [z0]

# Numerical solution using the explicit Euler method
while x_values[-1] < x_end:
    x_new = x_values[-1] + h
    y_new, z_new = f(x_values[-1], y_values[-1], z_values[-1])
    y_new *= h
    z_new *= h
    x_values.append(x_new)
    y_values.append(y_values[-1] + y_new)
    z_values.append(z_values[-1] + z_new)

# Convert the lists to NumPy arrays
x_values = np.array(x_values)
y_values = np.array(y_values)

# Plot the numerical solution
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Numerical Solution (Euler Method)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.title("Numerical Solution of d^2y/dx^2 + dy/dx + π^2y = 0 with Initial Conditions")
plt.show()
