import cv2
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#Every property has a number associated with it
#camera will set its avialable resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1208)
cap.set(4,620)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(4))

while (cap.isOpened()):
    ret,frame =(cap.read())
    if ret==True:

      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      cv2.imshow("frame",gray)

      if cv2.waitKey(1) & 0xFF == ord("q") :
          break
    else:
        break
cap.release()

cv2.destroyAllWindows()

