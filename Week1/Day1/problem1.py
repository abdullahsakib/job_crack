

import numpy as np

h1 = np.array([1200, 2, 15])  
h2 = np.array([1500, 3, 10])   
h3 = np.array([800, 1, 20]) 

w1, w2, w3 = 0.5, 0.3, 0.2

y = w1*h1 + w2*h2 + w3*h3

print (" Problem 1 Result :")
print ( f" Weighted House Vector : {y}\n")
print(f"Average size: {y[0]} sq.ft")
print(f"Average bedrooms: {y[1]}")
print(f"Average age: {y[2]} years")