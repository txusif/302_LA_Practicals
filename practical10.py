# Write a python program to enter a given matrix and calculate eigen value and eigen vector

import numpy as np
from numpy import linalg as LA

A = np.array([[1, 2, 3], [3, 2, 1], [1, 0, -1]])
w, v = LA.eig(A)
print("Eigen values:\n", w, end=" ")
print("\nEigen values:\n",v, end=" ")