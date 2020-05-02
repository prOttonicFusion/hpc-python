import numpy as np

# Two symmetric matrices
A = np.array([[1,2],[2,3]])
B = np.array([[4,5],[5,6]])
C = np.dot(A,B)


print('A = \n', A)
print('B = \n', B)
print('C = A DOT B = \n', C)
print('Eigenvalues of C: \n', np.linalg.eigvals(C))