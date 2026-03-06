print('Problen no 1:\n')

import numpy as np

A = np.array([
    [0.8, 0.3],
    [0.2, 0.7]
])


A_direct = np.linalg.matrix_power(A, 10)

print("A^10 using matrix_power:")
print(A_direct)

eigenvalues, Q = np.linalg.eig(A)

Lambda= np.diag(eigenvalues)

Lambda10=np.diag(eigenvalues**10)

Q_inv = np.linalg.inv(Q)

A_eigen = Q @ Lambda10 @ Q_inv

print("A^10 using eigen_values:")
print(A_eigen)



print('Problen no 2:\n')
np.random.seed(0)
X = np.random.randn(100,2)
cov_matrix = np.cov(X, rowvar=False)
print("Covariance Matrix:")
print(cov_matrix)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

idx = np.argmax(eigenvalues)

principal_vector = eigenvectors[:, idx]

print("Principal Eigenvector:")
print(principal_vector)

X_projected = X @ principal_vector

X_projected = X_projected.reshape(-1,1)

print("Projected Data Shape:")
print(X_projected.shape)


print('Problen no 3:\n')

S = np.array([
    [3,1],
    [1,3]
])

eigenvalues, eigenvectors = np.linalg.eig(S)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:\n")
print(eigenvectors)

v1 = eigenvectors[:,0]
v2 = eigenvectors[:,1]

dot_product = np.dot(v1, v2)

print("Dot Product:", dot_product)