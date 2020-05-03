import cv2
from matplotlib import pyplot as plt
import numpy as np


# img = cv2.imread("images/opencv_logo.png")
#img = cv2.imread("images/Noise_salt_and_pepper.png")
img = cv2.imread("images/lena.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernal=np.ones((5,5,),np.float32)/25
dstimg=cv2.filter2D(img,-1,kernal)
blur=cv2.blur(img,(5,5,))
guassianblur=cv2.GaussianBlur(img,(5,5,),0)
medianblur=cv2.medianBlur(img,5) #saltpepernoise blurring
bilateralFilter=cv2.bilateralFilter(img,9,75,75) #edge preserve


title=['image',"2d convolution","Averaging",'Gaussian', "median ","bilateralFilter"]
images=[img,dstimg,blur,guassianblur,medianblur,bilateralFilter]


for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([], plt.yticks([]))

plt.show()

