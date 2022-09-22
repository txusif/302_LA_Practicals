import numpy as np
u = np.array((3, 4, 5))
v = np.array((1, 2, 7))

print("Vector of u:", u)
print("Vector of v:", v)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

d = (a*u)+(b*v)
p = np.dot(u, v)

print("Vector au+bv:", d)
print("Dot product of u and v:", p)