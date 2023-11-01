import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation dy/dt = 0.2y
def f(t, y):
    return 0.2 * y

# Initial conditions
t0 = 0
y0 = 1  # Initial value of y
h = 0.2  # Step size
num_steps = 100  # Number of steps

# Create arrays to store the time and y values
t_values = [t0]
y_values = [y0]

# Perform the Euler method
for i in range(num_steps):
    t_i = t_values[-1]
    y_i = y_values[-1]
    y_iplus1 = y_i + h * f(t_i, y_i)
    t_values.append(t_i + h)
    y_values.append(y_iplus1)

# Plot the results
plt.plot(t_values, y_values)
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.title('Euler Method Solution for dy/dt = 0.2y')
plt.grid(True)
plt.show()
