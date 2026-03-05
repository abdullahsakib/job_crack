import numpy as np

def basis(n):
    matrix=[]

    for i in range(n):
        v=np.zeros(n)
        v[i]=1
        matrix.append(v)

    return matrix

B=basis(4)



print(B)
