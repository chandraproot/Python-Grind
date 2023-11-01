import numpy as np

# Define the matrix A (change this to your matrix)
A = np.array([[1, -1], [0, 0]])

# Check if A is a square matrix
if A.shape[0] == A.shape[1]:
    # Check if the dot product of all distinct rows is approximately zero
    rows_dot_product = np.dot(A, A.T)
    is_orthogonal = np.allclose(rows_dot_product, np.eye(A.shape[0]))

    # Check if the norm (magnitude) of each row is approximately 1
    row_norms = np.linalg.norm(A, axis=1)
    is_unit_length = np.allclose(row_norms, 1.0)

    # A matrix is orthogonal if both conditions are satisfied
    if is_orthogonal and is_unit_length:
        print("Matrix A is orthogonal.")
    else:
        print("Matrix A is not orthogonal.")
else:
    print("Matrix A is not square, so it cannot be orthogonal.")
