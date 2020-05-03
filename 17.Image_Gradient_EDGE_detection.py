import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("images/sudoku.jpg",cv2.IMREAD_GRAYSCALE)
lap =cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
#convert to unsigned int
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

#combine resul of sobel x and sobel y
sobelcombined=cv2.bitwise_or(sobelx,sobely)


title=['image',"Laplacian",'SobelX',"Spbely","sobelcombined"]
images=[img,lap,sobelx,sobely,sobelcombined]


for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([], plt.yticks([]))

plt.show()

