# Write a program to do the following:
# . Enter a vector u as a n-list
# . Enter another vector v as a n-list
# . Find the vector au + bv for different values of a and b
# . Find the dot product of u and v.

u = [2, 4, 3]
v = [3, 1, 5]

a = [4, 1, 3]
b = [2, 1, 4]

def add(u, v):
    return[a[i]*u[i]+b[i]*v[i] for i in range(len(u))]

print(add(u, v))
print(add(v, u))

def dot(u, v):
    sum1 = 0
    for n in range(len(u)):
        sum1 = sum1+u[n]*v[n]
    return sum1

print(dot(u, v))