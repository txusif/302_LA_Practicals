# WAP to do the following:
# 1.Enter an r by c Matrix M(r and c being positive integers)
# 2.Display M in matrix format
# 3.Display the rows and columns of matrix M
# 4.Find the scalar Multiplication of M
# 5.Find transpose of Matrix M

def printmatrix(A):
    for i in range(r):
        for j in range(c):
            print(A[i][j], end=" ")
        print()

def printrows(A):
    print("Row of matrix")
    for i in range(r):
        print("Row%d= " % i, A[i])

def printcolumns(A):
    print("Columns of matrix")
    for j in range(c):
        print("Column %d=" % j, end="  ")
        for i in range(r):
            print(A[i][j], end=" ")
        print(" ")

def scalarmul(A, s):
    N = [[s*A[i][j] for j in range(c)] for i in range(r)]
    print("The scalar multiplication s*M: ")
    printmatrix(N)

def transpose(A):
    T = [[A[i][j] for i in range(r)] for j in range(c)]
    print("Transpose of Matrix: ")
    for j in range(c):
        print(T[j])

print("Dimensions of matrix: ")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
M = []

for i in range(c):
    print("Enter elements of row",(i+1))
    M.append([])
    for j in range(c):
        n = int(input("Enter number: "))
        M[i].append(n)

print("Select operation")
print("1: Display Matrix")
print("2: Display Rows")
print("3: Display columns of matrix")
print("4: Scalar Multiplication")
print("5: Transpose of Matrix")
print("6: Exit")

while True:
    ch = int(input("Enter choice for operation: "))
    if ch == 1:
        printmatrix(M)
    elif ch == 2:
        printrows(M)
    elif ch == 3:
        printcolumns(M)
    elif ch == 4:
        sc = int(input("Enter scalar value: "))
        scalarmul(M, sc)
    elif ch == 5:
        transpose(M)
    elif ch == 6:
        break