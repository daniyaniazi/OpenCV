import cv2

#videocapture object
#1 2 for another cameras

cap = cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))#(name,fourcc_code,frames_per_second,size)

#to captures frames
while (True):
    ret,frame =(cap.read())#ret=if frame is availabe then true
    if ret==True:
      print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
      print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
      output.write(frame)#output the original_color video

      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#for greyscale
      cv2.imshow("frame",gray) #display the gray_scale video

      if cv2.waitKey(1) & 0xFF == ord("q") :
          break
    else:
        break
cap.release() #you need to release the resources of instances
output.release()
cv2.destroyAllWindows()

"""
#For path you need to check if video is is captured or not
#cv2.VideoCapture("path.mp4")
cap = cv2.VideoCapture(8)
print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = (cap.read())
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
cap.release() 
cv2.destroyAllWindows()"""