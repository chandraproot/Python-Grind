import numpy as np
t_array = [0.2, 0.5, 0.8, 0.9]
for t in t_array:
    # Define the matrix U and vector b
    U = np.array([[1, t, t],
                  [t, 1, t],
                  [t, t, 1]])

    b = np.array([2, 2, 2])

    # Initialize the solution vector x0 with zeros
    x0 = np.zeros(len(b))

    # Define the maximum number of iterations and tolerance
    max_iterations = 1000
    tolerance = 1e-6
    n = 0

    # Perform Gauss-Seidel iteration
    for iteration in range(max_iterations):
        x_new = np.copy(x0)

        for i in range(len(b)):
            x_new[i] = (b[i] - np.dot(U[i, :i], x_new[:i]) -
                        np.dot(U[i, i+1:], x0[i+1:])) / U[i, i]

        # Calculate the error
        error = np.linalg.norm(x_new - x0)

        # Update x0 with the new solution
        x0 = x_new
        n = n + 1

        # Check for convergence
        if error < tolerance:
            break

    # Print the result
    print(f"Number of iterations for {t} is {n}")
    print(f"Solution vector {x0}\n")
