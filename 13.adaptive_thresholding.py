#perivious thresholding set global thresholding value means it is same for the pixels of image
import cv2
import numpy as np

#thresholding calculating for smaller reigon of images
#whre image have different lightning conditions in different region
img =cv2.imread("images/sudoku.jpg",0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)

cv2.imshow("image",img)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",th2)
cv2.imshow("thresh3",th3)

#image have diff illumination region



cv2.waitKey(0)
cv2.destroyAllWindows()