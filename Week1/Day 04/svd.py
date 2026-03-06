import numpy as np

print('Problen no 1:\n')


np.random.seed(0)
X = np.random.randn(5,3)


U, S, VT = np.linalg.svd(X, full_matrices=False)

# convert singular values to diagonal matrix
Sd = np.diag(S)

print("Matrix X:")
print(X)

X_reconstructed = U @ Sd @ VT

print("Reconstructed X:")
print(X_reconstructed)

print("Reconstruction correct:\n", np.allclose(X, X_reconstructed))


print('Problen no 2:\n')
A = np.array([
    [3,1,1,0],
    [2,1,0,1],
    [4,1,2,1],
    [0,2,1,3],
    [1,0,2,2],
    [3,1,3,1]
])

U, S, VT = np.linalg.svd(A, full_matrices=False)

print("Singular Values:")
print(S)

k = 2

U_k = U[:, :k]
S_k = np.diag(S[:k])
VT_k = VT[:k, :]

A_k = U_k @ S_k @ VT_k

print("Compressed Matrix A_k:")
print(A_k)

loss = np.linalg.norm(A - A_k, 'fro')

print("Information lost (Frobenius norm):")
print(loss)


print('Problen no 3:\n')

np.random.seed(12)
X = np.random.randn(100,3)

X_centered = X - np.mean(X, axis=0)

print("Column means after centering:")
print(np.mean(X_centered, axis=0))

U, S, VT = np.linalg.svd(X_centered, full_matrices=False)

print("V^T:")
print(VT)

cov_matrix = np.cov(X_centered, rowvar=False)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("Eigenvectors of covariance matrix:")
print(eigenvectors)