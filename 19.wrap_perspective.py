import cv2
import  numpy as np

width,height=250,350 #card ratio
img=cv2.imread("images/cards.jpg",1)
# points obtained from paint
points=np.float32([[111,219],[287,188],[154,482],[352,440]])
# Define which corner are we refering(mapping our points)
points2=np.float32([[0,0],[width,0],[0,height],[width,height]])
# Transformation matrix
matrix=cv2.getPerspectiveTransform(points,points2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Wrap image",imgOut)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()