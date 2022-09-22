# Write a program which demonstrates the following: 
# A. Addition of two complex numbers 

a = 2+3j
b = 4+2j

sum = a+b
print(sum)
u = complex(3, 2)

print("U =", u)
print("real number of u:", u.real)
print("imaginary part of u:", u.imag)

v = complex(4, -3)
print("V =", v)
print("Real part of v:", v.real)
print("Imaginary part of v:", v.imag)

print("Addition of u and v is: ", u+v)
print("Subtraction of u and v is: ", u-v)
print("Multiplication of u and v is: ", u*v)
print("Division of u and v is: ", u/v)