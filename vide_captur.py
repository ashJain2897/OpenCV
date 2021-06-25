#Author ASH
#July 2019

import numpy as np
import cv2
import os
import io



user=raw_input("Can I know your name??")
print"Your name is-->",user


status=input("Is your name right??")

if(status):

 #Include path
 os.mkdir('/home/ash/Desktop/'+str(user))
 cap = cv2.VideoCapture(0)
 d=0
 while(True):
     # Capture frame-by-frame
     ret, frame = cap.read()
     
     # Our operations on the frame come here
     gray = cv2.cvtColor(frame, 0)
 
     # Display the resulting frame
     cv2.imshow('frame',gray)
     
     if d<=25: 
      filename = "/home/ash/Desktop/"+str(user)+"/file_%d.jpg"%d
      cv2.imwrite(filename, frame)
      d+=1
    	   
     if cv2.waitKey(1) & 0xFF == ord('q'):
    
         break

 # When everything done, release the capture
 cap.release()
 cv2.destroyAllWindows()


#filename = "/home/ash/Desktop/ash/file_%d.jpg"%d
 #   cv2.imwrite(filename, frame)
  #  d+=1
  

