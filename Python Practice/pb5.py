import numpy as np
from scipy.linalg import solve
from scipy.special import gamma
from scipy.misc import factorial
from math import cos, sin, pi

# Function to calculate the biharmonic term
def biharmonic(y, z, n, m, alpha, beta):
    term1 = (-1)**(n+m+1) * gamma(n+1) * gamma(m+1)
    term2 = factorial(2*n+1) * factorial(2*m+1)
    term3 = (2*alpha)**(2*n+1) * (2*beta)**(2*m+1)
    term4 = (1-cos(n*pi*y/alpha)) * (1-cos(m*pi*z/beta))
    term5 = sin(n*pi*y/alpha) * sin(m*pi*z/beta)
    return term1/term2 * term3/term4 * term5

# Parameters
alpha = 1 # x length
beta = 1 # y length
ny = 50 # number of y intervals
nz = 50 # number of z intervals
nu = 1 # pressure gradient
mu = 1 # viscosity

# Grid points
y = np.linspace(-alpha, alpha, ny+1)
z = np.linspace(-beta, beta, nz+1)

# Calculate the coefficients of the system of linear equations
coefficients = np.zeros((ny+1, nz+1))
for i in range(1, ny, 2):
    for j in range(1, nz, 2):
        coefficients[i, j] = -mu * biharmonic(y[i], z[j]),