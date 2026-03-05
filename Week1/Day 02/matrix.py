#number 1
import numpy as np
A = np.array([
            [1, 2],
            [3, 4]
            ])

B = np.array([ [0, 1],
               [-1, 0]
            ])


AB=A@B
BA=B@A


element_wise=A*B

print(f"AB: \n{AB}")
print(f"BA: \n{BA}")

print(f"element_wise: \n{element_wise}")


print("Problem 2:")


X = np.array([
    [1, 1],
    [2, 1],
    [2, 2],
    [1, 2],
    [1.5, 1.5]
])


S = np.array([
    [1, 1.5],
    [0, 1]
])


X_transformed = (S @ X.T).T


print(f"transformed_matrix: \n{X_transformed}")


print("Problem 3:")

#according to question
A = np.array([
            [3, 2],
            [1, 4]
            ])

B = np.array([28, 16])

prices=np.linalg.solve(A,B)

print ( f"GPU Price per hour : ${ prices [0]:.2f}")
print ( f"CPU Price per hour : ${ prices [1]:.2f}")


