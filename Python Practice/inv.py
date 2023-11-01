import numpy as np
A = np.array([[1, 2], [2, 2]])
A_inv = np.linalg.inv(A)
print(A_inv)

B = np.array([[6, 4], [3, 3]])
B_inv = np.linalg.inv(B)
# print(B_inv)

AB = np.dot(A, B)
# print(AB)

AB_inv = np.linalg.inv(AB)
# print(AB_inv)

BA = np.dot(B_inv, A_inv)
# print(BA)
