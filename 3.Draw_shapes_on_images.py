import cv2
import numpy as np
#CREATE A BLACK IMG USING NUMPY ARRAYS
# img=np.zeros([512,512,3],np.uint8)
img=cv2.imread("images/lena.jpg",1)
img=cv2.line(img,(0,0), (255,255), (255,0,0),10)#bgr format
img=cv2.arrowedLine(img,(0,255), (255,255), (255,255,0),10)
#rectangle
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255), -1)
img=cv2.rectangle(img,(84,0),(51,18),(0,0,255), 10)
#circle
img=cv2.circle(img,(447,63),63,(0,255,0),-1)
#put text on image
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,"OpenCV",(10,500),font ,2, (0,255,255),5,cv2.LINE_AA)
#draw polygons
penta = np.array([[[40,160],[120,100],[200,160],[160,240],[80,240]]], np.int32)
triangle = np.array([[[240, 130], [380, 230], [190, 280]]], np.int32)
img=cv2.polylines(img, [triangle], True, (0,255,0), thickness=3)
img = cv2.polylines(img, [penta], True, (255,120,255),3)
cv2.imshow("image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()