import numpy as np

A = np.array([[4, -5],[-2, 3]])

B = np.array([[-13], [9]])

x = np.linalg.inv(A).dot(B)

print(x)

A = np.asmatrix(A)
B = np.asmatrix(B)

x = A.I*B

print(x)