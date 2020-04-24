#create polygons on images using mouse click
import cv2

def click_event(event,x,y,flags,param):
    if event== cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        print(points)
        if len(points)>=2:
            cv2.line(img,points[-2],points[-1],(255,0,0,),5)
        cv2.imshow("image",img)



img=cv2.imread("images/lena.jpg",1)
cv2.imshow("image",img)
points=[]
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()