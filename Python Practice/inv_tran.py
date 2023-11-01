import numpy as np
A = np.array([[2, 3], [5, 6]])
A_inv = np.linalg.inv(A)
A_inv_tran = np.round(np.transpose(A_inv))
print(np.round(A_inv_tran))

A_tran = np.transpose(A)
A_tran_inv = np.round(np.linalg.inv(A_tran))
print(np.round(A_tran_inv))


if np.array_equal(A_inv_tran, A_tran_inv):
    print("Matrices A and B are equal.")
else:
    print("Matrices A and B are not equal.")
