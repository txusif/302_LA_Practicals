# D. Creating a new plot by rotating the given number by a degree 90, 180, 270 degrees 
# and also by scaling by a number a = 1/2, a = 1/3, a = 2 etc.

# 90 Degree

import matplotlib.pyplot as plt
x = 2+4j
z = -1j
plt.scatter(x.real, x.imag, color='red')
c = x*z
plt.scatter(c.real, c.imag, color='blue')
plt.show()