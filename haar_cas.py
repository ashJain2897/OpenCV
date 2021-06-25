#Title:Face detection and create face data
#Author:ASH
#Explanation :- The following code captures the face data using web cam and hence stores in a user direectory ising opencv and haar cascade.

#Packages used:-

import cv2
import sys
import numpy
import os
import io

#haar cascade file to detect face co-ordinates 
haar_file = 'haarcascade_frontalface_default.xml'

# All the faces data will be 
# User data present in this folder
datasets = 'datasets'

#Asks Users name and take user name as input which will create a directory of the user entered.
user=raw_input("Can I know your name??")
print"Your name is-->",user

#confirms user name
status=input("Is your name right??")

if(status):
 os.mkdir('/home/ash/HAAr/Face_Detect_final/datasets/'+str(user))


# These are sub data sets of folder,  
# User label 
sub_data = str(user)	

path = os.path.join(datasets, sub_data)  

# defines the size of images.
(width, height) = (130, 100)	 

#'0' is used for my webcam, 
#'1' used for other camera
#include .xml in face_cascade
face_cascade = cv2.CascadeClassifier(haar_file) 
webcam = cv2.VideoCapture(0) 

# loops for 30 faces  
counter = 1
while counter < 30: 
	(_, im) = webcam.read() 
	gray = cv2.cvtColor(im, 0) #flag set as 0 for normal webcam.
	 
	faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
	#coordinates for face edges.
	for (x, y, w, h) in faces: 
		cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
		face = gray[y:y + h, x:x + w] 
		face_resize = cv2.resize(face, (width, height)) 
		cv2.imwrite('% s/% s.png' % (path, counter), face_resize)#stores the image in user directory 
	counter += 1
	
	cv2.imshow('OpenCV', im) 
	key = cv2.waitKey(10) 
	if key == 27: 
		break

