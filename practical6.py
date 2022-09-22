# Basic Matrix Application – II
# Perform Image addition, multiplication and subtraction.

import cv2
import matplotlib
from matplotlib import pyplot as plt

img1 = cv2.imread("naruto1.jpg")
img2 = cv2.imread("itachi.jpg")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

height, width, color_scale = img1.shape
dim = (width, height)

img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

print("Original Dimension img1:", img1.shape)
print("Original Dimension img2:", img2.shape)

add_img = cv2.add(img1, img2)
sub_img = cv2.subtract(img1, img2)
mul_img = cv2.multiply(img1, img2)

titles = ['image1', 'image2', 'added image', 'image1', 'image2',
          'subtract image', 'image1', 'image2', 'multiply image']
images = [img1, img2, add_img, img1, img2, sub_img, img1, img2, mul_img]

for i in range(9):
    plt.subplot(3, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()