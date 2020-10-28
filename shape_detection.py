import cv2
import numpy as np

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    objecType=''
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgCopy,cnt,-1,(255,0,255),3)
            peri=cv2.arcLength(cnt,True)
            print(peri)
            # Approximate corner points contour,resolution,closed
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
            if objCor == 3: objecType = 'Triangle'
            elif objCor == 4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio < 1.05:
                    objecType = 'Square'
                else:
                    objecType = 'Rectangle'
            elif objCor > 4 and objCor  <8 :objecType = 'Polygon'
            elif objCor>7:
                objecType = 'Circle'


            cv2.rectangle(imgCopy,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(imgCopy,objecType,(int(x+(w/2)-30),int(y+(h/2))), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,200,200),1)


img=cv2.imread("images/shapes.png",1)
print(img.shape)
img=cv2.resize(img,(img.shape[0]*3,img.shape[1]* 2))
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
imgCopy=img.copy()
getContours(imgCanny)

cv2.imshow("image",img)
cv2.imshow("imgGray",imgGray)
cv2.imshow("imgBlur",imgBlur)
cv2.imshow("imgBlur",imgCanny)
cv2.imshow("imgCopy ",imgCopy)
cv2.waitKey(0)
cv2.destroyAllWindows()