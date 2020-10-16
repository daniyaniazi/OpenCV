import cv2
import os
import numpy as np
import faceRecongnition as fr

test_img= cv2.imread('C:\\Users\\DANIA NIAZI\\Desktop\\GIT_PROJECTS\\OpenCV\\Face Recongnition\\testImages\\face11.jpg')
faces_detected,gray_img=fr.faceDetection(test_img)
print("face_dtected:", faces_detected)

#calling the label for training data
# faces,faceIDLabels = fr.labels_for_training_data('C:\\Users\\DANIA NIAZI\\Desktop\\GIT_PROJECTS\\OpenCV\\Face Recongnition\\trainingData')
#TRAINING CLASSIFIER
# face_recognizer=fr.train_classifier(faces,faceIDLabels)
#Save classifer
# face_recognizer.save('TrainingData.yml' )

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:\\Users\\DANIA NIAZI\\Desktop\\GIT_PROJECTS\\OpenCV\\Face Recongnition\\TrainingData.yml')

#labelling
name={0:'Engin',
      1: 'Cengiz'}
    
for face in faces_detected: #taking the first face which is detected
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+w,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    #0=exact match if confidence is above 35 we are not going to do prediction
    print('confidence :', confidence)
    print('Label :',label)
    #if(confidence>37):
     #   fr.draw_rect(test_img,face)
      #  fr.put_text(test_img, 'NotFound',x,y)
       # continue
    #Drawing a rectangle on test image 
    fr.draw_rect(test_img,face)
    predicted_name=name[label] #Text from dic
    #Adding text at top left corner
    fr.put_text(test_img, predicted_name,x,y)
    
    
resized_img= cv2.resize(test_img,(800,700))
cv2.imshow('Face Detection' , resized_img);
cv2.waitKey(0)
cv2.destroyAllWindows()














#for (x,y,w,h) in faces_detected:
 #   cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)
    
#resized_img= cv2.resize(test_img,(1000,700))
#cv2.imshow('Face Detection' , resized_img);
#cv2.waitKey(0)
#cv2.destroyAllWidows

