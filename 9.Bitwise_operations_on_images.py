import cv2
import numpy as np

"bitwise operators can be very useful when working with masks ." \
"masks are binary images that indicates the pixels in which an operation is to be perfomed"
img1=cv2.imread("images/BW.PNG")
img2=np.zeros((250,578,3),np.uint8)
rec=cv2.rectangle(img2,(248,0),(328,80),(255,255,255),-1)#CREATE A WHITE REC INSIDE A BLACK IMAGE CREATED BY NUMPY
#same as img dimension

#BITWISE OPERATIONS
bitand=cv2.bitwise_and(img1,img2)
#black=0
#white=1
bitor=cv2.bitwise_or(img1,img2)
bitxor=cv2.bitwise_xor(img1,img2)
bitnot=cv2.bitwise_not(img1)

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("and",bitand)
cv2.imshow("or",bitor)
cv2.imshow("xor",bitxor)
cv2.imshow("not",bitnot)

cv2.waitKey(0)
cv2.destroyAllWindows()


