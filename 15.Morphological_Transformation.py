import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("images/smart1.PNG",cv2.IMREAD_GRAYSCALE)

ret,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8) #sqaue 2 by 2
dialation=cv2.dilate(mask,kernal,iterations=2) #for removing spots
erosion=cv2.erode(mask,kernal,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
grad=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)

title=['image',"mask","dilation",'erosion',"opening",'closing',"GRADIENT"]
images=[img,mask,dialation,erosion,opening,closing,grad]
#Morphological_Transformation are perfomed on binary images thats why we need to perform thresholding

for i in range(7):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([], plt.yticks([]))

plt.show()