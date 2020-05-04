import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("../images/faceman.jpg",cv2.IMREAD_GRAYSCALE)


kernal=np.array([[-1,-1,-1],[-1,9,-1], [-1,-1,-1]])

sharped=cv2.filter2D(img,-1,kernal)
inv=255-img
guass=cv2.GaussianBlur(inv,ksize=(59,59),sigmaX=0,sigmaY=0)

sketch=cv2.divide(img,255-guass,scale=257)








title=['image',"sharped","inverse","guass","sketch"]
images=[img,sharped,inv,guass,sketch]

for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(title[i])
    plt.xticks([], plt.yticks([]))

plt.show()