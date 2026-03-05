

import numpy as np

X = np.array([
    [0, 30, 32],
    [10, 45, 50],
    [20, 60, 68],
    [30, 50, 86],
    [40, 70, 104]
])


# here x3​=1.8⋅x1​+32
X_new=X.copy()
X_new[:,2]=X[:,2]-32

print(X_new)

rank_X = np.linalg.matrix_rank(X_new)

print(f"rank of the matrix is {rank_X}")

#The features are linearly dependent (rank < number of features)