# Basic Matrix Application – I
# Representation of Image in Matrix Format and Image Transformations.

import numpy as np
from PIL import Image
a = Image.open("naruto.jpg")
b = Image.open("thorfinn.jpg")
a.show()
b.show()
i1 = np.asarray(a)
i2 = np.asarray(b)
print("Co-ordinates of img1\n", i1)
print("Co-ordinates of img1\n", i2)