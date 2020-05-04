import cv2
from matplotlib import pyplot as plt
import numpy as np
"""
COMPOSED OF 5 STEPS:
1.Noise Reduction
2.Gradient Calculation
3.Non_Maximum Supression
4.Double threshold
5.Edge Tracking by Hysteresis
"""
img = cv2.imread("images/lena.jpg",cv2.IMREAD_GRAYSCALE)
canny=cv2.Canny(img,100,200)
ret,thresh1=cv2.threshold(canny,0,255,cv2.THRESH_BINARY_INV)

title=['image',"Canny","binarythrs"]
images=[img,canny,thresh1]


for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([], plt.yticks([]))

plt.show()
