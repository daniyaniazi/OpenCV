# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:29:46 2020

@author: DANIA NIAZI
"""

import cv2
import os
import numpy as np

def faceDetection(test_img):
   
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    #To avoid dostracting features 
    face_haar_cascade= cv2.CascadeClassifier('C:\\Users\\DANIA NIAZI\\Desktop\\GIT_PROJECTS\\OpenCV\\Face Recongnition\\HaarCascade\\haarcascade_frontalface_default.xml')
    faces= face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)
    return faces,gray_img

#Generate Labels for each of image of our training data
def labels_for_training_data(directory): #Haar classifier accepts images with integars lables 
    faces=[]
    faceIDLabels=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")#skiping no needed file file like .gitigonre etc
                continue

            id=os.path.basename(path)#fetching subdirectory names
            img_path=os.path.join(path,filename)#fetching image path
            print("img_path:",img_path)
            print("id:",id)
            #Image loading 
            test_img=cv2.imread(img_path)
            
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img)
            if len(faces_rect)!=1:
               continue #Image with only one face assuming
            (x,y,w,h)=faces_rect[0]
            #Exracting face from he image
            roi_gray=gray_img[y:y+w,x:x+h]
            faces.append(roi_gray)
            faceIDLabels.append(int(id))
    return faces,faceIDLabels
    
#Training our classifier
def train_classifier(faces,faceIDLabels):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    #Local Binary Pattern histogram , central pixel is comparing with surronding pixel for generating binary pattern and then extract histogram from created image
    face_recognizer.train(faces,np.array(faceIDLabels))
    #take labels as numpy array cuz Ml work on numpy array 
    return face_recognizer

#Function to draw bounding box arround the detected face
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)
#adding text lablel on image'
    
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x-60,y+120),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
    


    

