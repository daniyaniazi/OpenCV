import cv2
import numpy as np
framewidth=640
farmeheight=480
cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,farmeheight)
cap.set(10,150)
# Def list of colors that we want to detect

myColor=[[22,92,112 ,179 ,255 ,253],
         [72,81,94,179,255,166]]

# BGR
myColorValues=[(47,255,173),(255,144,30)]
# Draw Points
drawPoints=[]  #x,y,colorId
newPoints=[]

def findColor(img,myColor,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    colorCount=0
    for color in myColor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getContours(mask)
        cv2.circle(imgCopy,(x,y),5,myColorValues[colorCount],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,colorCount])
        colorCount+=1
    return newPoints
        # cv2.imshow(str(color[0]), mask)

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imgCopy,cnt,-1,(255,0,255),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
            # cv2.rectangle(imgCopy, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return x+w//2 , y

def DrawCanvas(drawPoints,myColorValues):
    for points in drawPoints:
        print(points)
        cv2.circle(imgCopy, (points[0], points[1]), 10, myColorValues[points[2]], cv2.FILLED)


while (True):
    getPoints=list()
    ret,img =(cap.read())
    imgCopy=img.copy()
    newPoints=findColor(img,myColor,myColorValues)
    # print('New Points',newPoints)
    # if len(newPoints)!=0:
    #     for points in newPoints:
    #          getPoints.append(points)
    # if len(getPoints)!=0:
    #     DrawCanvas(getPoints,myColorValues)
    for points in newPoints:
        print(points)
        cv2.circle(imgCopy, (points[0], points[1]), 10, myColorValues[points[2]], cv2.FILLED)
    cv2.imshow("frame", imgCopy)
    if cv2.waitKey(1) & 0xFF == ord("q") :
          break
