import cv2
from matplotlib import pyplot as plt

import numpy as np

img =cv2.imread("images/gradient.jpg",0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles=["original image","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]
images=([img,thresh1,thresh2,thresh3,thresh4,thresh5])
for i in range(6):
    # rows and col
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
plt.show()
# cv2.imshow("image",img)
# cv2.imshow("thresh1",thresh1)
# cv2.imshow("thresh2",thresh2)
# cv2.imshow("thresh3",thresh3)
# cv2.imshow("thresh4",thresh4)
# cv2.imshow("thresh5",thresh5)


# cv2.waitKey(0)
# cv2.destroyAllWindows()