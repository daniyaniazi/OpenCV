import cv2
import  numpy as np

img=cv2.imread("images/cards.jpg",1)
# Both images have same no of  channel
hor=np.hstack((img,img))
ver=np.vstack((img,img))
cv2.imshow('Horizontal stack',hor)
cv2.imshow('ver stack',ver)
cv2.waitKey(0)
cv2.destroyAllWindows()