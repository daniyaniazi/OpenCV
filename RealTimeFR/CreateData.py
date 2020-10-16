import cv2,os
haar_file='C:\\Users\\DANIA NIAZI\\Desktop\\GIT_PROJECTS\\OpenCV\\Face Recongnition\\HaarCascade\\haarcascade_frontalface_default.xml'
dataset='datasets'
#Which person dataset
subdata='Daniya'

path=os.path.join(dataset,subdata)
#If path is available or not
if not os.path.isdir(path):
    os.mkdir(path)

(width,height)=(130,100)
#uploaded haar alogrithm to classifier
face_cascade=cv2.CascadeClassifier(haar_file)
#initialize camera
webcam=cv2.VideoCapture(0)
print(webcam)
count=1
while count<31: #Capturing 30 images
    print(count)
    (ret,img)=webcam.read() #read camera

    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # grayscale img
    facesFound= face_cascade.detectMultiScale(gray_img,1.32,3) #get coordinates of faces
    for (x,y,w,h) in facesFound:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle arround faces found
        faceFound=gray_img[y:y+h,x:x+w] #crop face part for dataset
        face_resized=cv2.resize(faceFound,(width,height))
        cv2.imwrite('%s/%s.png'%(path,count),face_resized)
    count+=1

    cv2.imshow('Face',img)
    key=cv2.waitKey(10)
    if key==27:
        break

webcam.release()
cv2.destroyAllWindows()

