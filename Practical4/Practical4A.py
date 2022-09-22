# WAP to do the following
# Enter the positive number N and
# 1) FIne the number 'a' and 'b' such that a^2-b^2=N
# 2)Find the GCD of two numbers using Euclid's Algorithm.

N = 28
a = 7
b = 4
print("The value of positive Number N is: ", N)
print("Factors of N are: ", a, b)
x = (a+b)/2
y = (a-b)/2

print("The value of x : ", x)
print("The value of y : ", y)

asqr = x*x
bsqr = y*y

print("The value of square x : ", asqr)
print("The value of square y: ", bsqr)

N = asqr - bsqr
print(N)