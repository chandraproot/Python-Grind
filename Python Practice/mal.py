# Define the function f(x) and its derivative f'(x)
def f(x):
    return x**3 + 2*x**2 - 3*x - 4


def f_prime(x):
    return 3*x**2 + 4*x - 3


# Initial guess value
x0 = 1.5

# Set tolerance for convergence
tolerance = 1e-6

# Maximum number of iterations
max_iterations = 100

# Initialize variables
x = x0
iterations = 0

# Newton-Raphson iteration
while iterations < max_iterations:
    # Calculate the next approximation using the formula x - f(x) / f'(x)
    x_new = x - f(x) / f_prime(x)

    # Check for convergence by comparing the absolute difference between x_new and x
    if abs(x_new - x) < tolerance:
        break

    # Update x for the next iteration
    x = x_new
    iterations += 1

# Check if the loop terminated due to convergence or reached the maximum iterations
if iterations < max_iterations:
    print(f"Root found: x = {x_new}")
    print(f"Number of iterations: {iterations}")
else:
    print("The method did not converge within the maximum number of iterations.")
