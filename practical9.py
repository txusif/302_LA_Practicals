# Write a program to implement Row echelon form(order 2).
# A matrix is in row echelon form
# 1. The first non-zero element in each row is called leading entry and is 1.
# 2. Each leading entry is in a column to the right of the leading entry is the previous row.
# 3. Rows with all zero elements if any are below the rows having a non-zero element. 

from sympy import * 
m = Matrix([[1, 2, 1], [0, 1, 2],[1, 1, 1]])
print(m)
print(m.rref())

# (rref)Reduced Row Echelon Form conditions:
# 1. The matrix should be in row echelon form(it satisfies the 3 conditions listed above).
# 2. The leading entry in each row is the only non-zero entry in its column.