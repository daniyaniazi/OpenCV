import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("../images/faceman.jpg",cv2.IMREAD_GRAYSCALE)

bilateralFilter=cv2.bilateralFilter(img,1,5,5)
canny=cv2.Canny(bilateralFilter,100,200)
ret,thresh1=cv2.threshold(canny,0,255,cv2.THRESH_BINARY_INV)

title=['image',"bilateralFilter","Canny","binary thrs",]
images=[img,bilateralFilter,canny,thresh1]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([], plt.yticks([]))

plt.show()

# bilateralFilter=cv2.bilateralFilter(img,9,75,75)
# guassianblur=cv2.GaussianBlur(img,(1,1,),0)
# kernal=np.ones((2,2,),np.float32)/4
# dstimg=cv2.filter2D(img,-1,kernal)