# 270 Degree

import matplotlib.pyplot as plt
x = 2+4j
scale = 0.5
scale1 = 0.33
scale2 = 2
plt.scatter(x.real, x.imag, color="red")
# rotation by 270 degree
c = scale*x
d = scale1*x
e = scale2*x
plt.scatter(c.real, c.imag, color="blue")
plt.scatter(d.real, d.imag, color="black")
plt.scatter(e.real, e.imag, color="green")
plt.show()