import numpy as np
import matplotlib.pyplot as plt

# Define the exact solution
def yexact(x):
    return np.sin(2*np.pi*x)

# Define the first order Euler explicit method
def euler_explicit(f, x0, y0, h, x):
    y = np.zeros_like(x)
    y[0] = y0
    for i in range(1, len(x)):
        y[i] = y[i-1] + h * f(x[i-1], y[i-1])
    return y

# Define the second order Runge-Kutta method
def rk2(f, x0, y0, h, x):
    y = np.zeros_like(x)
    y[0] = y0
    for i in range(1, len(x)):
        k1 = h * f(x[i-1], y[i-1])
        k2 = h * f(x[i-1] + h/2, y[i-1] + k1/2)
        y[i] = y[i-1] + h * (k1 + k2) / 2
    return y

# Define the error function
def error(y, yexact):
    return np.max(np.abs(y - yexact))

# Define the range of step sizes
h_min = 0.01
h_max = 0.1
h_vals = np.linspace(h_min, h_max, 100)

# Compute the errors for Euler explicit and RK2 methods
errors_euler = []
errors_rk2 = []

for h in h_vals:
    x = np.linspace(0, 10, int(10/h) + 1)
    y = euler_explicit(lambda x, y: 2*np.pi*np.cos(2*np.pi*x)*y, 0, 1, h, x)
    errors_euler.append(error(y, yexact(x)))

    y = rk2(lambda x, y: 2*np.pi*np.cos(2*np.pi*x)*y, 0, 1, h, x)
    errors_rk2.append(error(y, yexact(x)))

# Plot the errors
plt.plot(h_vals, errors_euler, label='Euler Explicit')
plt.plot(h_vals, errors_rk2, label='RK2')
plt.xlabel('Step size (h)')
plt.ylabel('Solution error (ϵ)')
plt.title('Solution error vs. step size for Euler explicit and RK2 methods')
plt.legend()
plt.grid(True)
plt.show()
