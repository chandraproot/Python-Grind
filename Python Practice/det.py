import numpy as np

A = np.array([[8, 6, 1], [4, 6, 7], [7, 3, 9]])
A_det = np.round(np.linalg.det(A), decimals=3)
print("The determinant of the matrix A is", A_det)
