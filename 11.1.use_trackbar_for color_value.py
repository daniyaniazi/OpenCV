import cv2
import numpy as np

#there are more than 150 color space conversion method and one of them is coloured image to hsv image

def nothing(x):
    pass


cv2.namedWindow("tracking")
cv2.createTrackbar("lh","tracking",0,255,nothing)
cv2.createTrackbar("uh","tracking",255,255,nothing)

cv2.createTrackbar("ls","tracking",0,255,nothing)
cv2.createTrackbar("us","tracking",255,255,nothing)

cv2.createTrackbar("lv","tracking",0,255,nothing)
cv2.createTrackbar("uv","tracking",255,255,nothing)


while True:
    frame=cv2.imread("images/smarties.jpg")
    #convert a color image to hsv images
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("lh","tracking")
    l_s = cv2.getTrackbarPos("ls", "tracking")
    l_v = cv2.getTrackbarPos("lv", "tracking")

    u_h = cv2.getTrackbarPos("uh", "tracking")
    u_s = cv2.getTrackbarPos("us", "tracking")
    u_v = cv2.getTrackbarPos("uv", "tracking")




    #THRESHOLD a  hsv image for a range of bliue color
    lower_blue=np.array([l_h,l_s,l_v,]) ##define lower range of blue color
    #we can use tract bar to detect the lower and upper value of  hsvcolor space
    upper_blue = np.array([u_h,u_s,u_v, ])
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