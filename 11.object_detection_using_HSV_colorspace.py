import cv2
import numpy as np

#there are more than 150 color space conversion method and one of them is coloured image to hsv image

def nothing(x):
    pass


# cv2.namedWindow("tracking")

while True:
    frame=cv2.imread("images/smarties.jpg")
    #convert a color image to hsv images
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #THRESHOLD a  hsv image for a range of bliue color
    lower_blue=np.array([110,50,50,]) ##define lower range of blue color
    #we can use tract bar to detect the lower and upper value of  hsvcolor space
    upper_blue = np.array([130, 255,255, ])
    #therhold the hsv image to get only blue image
    mask= cv2.inRange(hsv,lower_blue,upper_blue)

    #to mask the original image use bitwise operation
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)


    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()