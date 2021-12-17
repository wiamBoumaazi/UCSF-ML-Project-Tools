# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 19:21:18 2020
@author: hjsong
Purpose : video viewer to pause/continue/back/forward navigation
How to use : p (pause)  c (continue)  q(quit) 
             once you pause mode, you can b(back) and n(next).  
             
             For you to exit pause, you have to press c(continue.)  
             If you would like to adjust buffer size to navigate, adjust buffer_size var in the below
             If you would like to adjust play speed, adjust labTime var in the below.
             Where to locate video file : refer to cap var.
"""

import cv2
import numpy as np
import dlib
# edited: Added imports as in head_pose_estimation.py
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sys
import time

from numpy.core.fromnumeric import shape
from scipy.signal import savgol_filter

#wiam
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# read nose tip file and store values in a list
noseTip_file_path= '/Users/wiamboumaazi/Desktop/HeadPose:Gaze/nosetip'
noseTip_lines = []
noseTip_values =[]
with open(noseTip_file_path) as file_in:
    for line in file_in:
        noseTip_lines.append(line)

for i in range(0, len(noseTip_lines)):
   noseTip_values.append(noseTip_lines[i].split("  "))


# read headpose file and store values in a list
headPose_file_path= '/Users/wiamboumaazi/Desktop/HeadPose:Gaze/headpose'
headPose_lines = []
headPose_values =[]
with open(headPose_file_path) as file_in:
    for line in file_in:
        headPose_lines.append(line)

for i in range(0, len(headPose_lines)):
   headPose_values.append(headPose_lines[i].split("  "))

#READ Normalized Gaze values
GazeNormalized_file_path= '/Users/wiamboumaazi/Desktop/HeadPose:Gaze/Adam_gaze'
GazeNormalized_lines = []
GazeNormalized_values =[]
with open(GazeNormalized_file_path) as file_in:
    for line in file_in:
        GazeNormalized_lines.append(line)

for i in range(0, len(GazeNormalized_lines)):
   GazeNormalized_values.append(GazeNormalized_lines[i].split("  "))

#READ DeNormalized Gaze values
GazeDeNormalized_file_path= '/Users/wiamboumaazi/Desktop/HeadPose:Gaze/Adam_gaze2'
GazeDeNormalized_lines = []
GazeDeNormalized_values =[]
with open(GazeDeNormalized_file_path) as file_in:
    for line in file_in:
        GazeDeNormalized_lines.append(line)

for i in range(0, len(GazeDeNormalized_lines)):
   GazeDeNormalized_values.append(GazeDeNormalized_lines[i].split("  "))


#for n in range(len(GazeDeNormalized_values)):
    #print(GazeDeNormalized_values[n][3])

#for n in range(len(headPose_values)):
    #print(headPose_values[n][3])

#for n in range(len(noseTip_values)):
    #print(noseTip_values[n][0])

cap = cv2.VideoCapture('/Users/wiamboumaazi/Desktop/HeadPose:Gaze/AGportrait28withsidelight.mov')
ret, img = cap.read()
thresh = img.copy()

cv2.namedWindow('image')
#kernel = np.ones((9, 9), np.uint8)


fIndex=-1   # frame index

def nothing(x):
    pass


# edit
#cv2.createTrackbar('threshold', 'image', 40, 255, nothing)

#hjsong put the image buffer to track back 
buffer_size=40   # could increase buffer_size as you wish
lapTime=0.1    # lab between the consecutive frames 
bi=-1
imgBuffer = np.arange (buffer_size* img.shape[0]*img.shape[1]*img.shape[2],  dtype=np.uint8).reshape(-1, img.shape[0], img.shape[1], img.shape[2])

while(True):

    bi = (bi + 1 ) %  buffer_size  # buffer index 
    imgBuffer[bi] = img

    ret, img = cap.read()
    time.sleep(lapTime)  # to slow down the video play
    fIndex+=1
    #wiam

    

    if ret == True :   
        #for i in range(len(list2)):
            #if fIndex == list2[i][0]:
                #cv2.putText(img, 'fIndex' +str(list2[fIndex][1])+ ' '+ str(list2[][1]), (90, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 128), 3) 
        #wiam
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            landmarks = predictor(gray, face)
            landmarks = predictor(gray, face)
            index = 0
            landmark_list = {}
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

            """
            for i in landmarks.parts():
                cords = (int(str(i).split(",")[0][1:]),int(str(i).split(",")[1][:-1]))
                landmark_list[str(index)] = cords
                index +=1
            """
        cv2.putText(img, ' "fIndex" ' +str(fIndex), (90, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)        
        #cv2.putText(img, 'noseTip (pixel): ' +str(int(noseTip_values[fIndex][1])), (90, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)
        #cv2.putText (img, 'DeltanoseTip' + str(abs(int(noseTip_values[fIndex][1]) - int(noseTip_values[fIndex-1][1]))), (90, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 128), 3) 
        #cv2.putText(img, 'HeadYaw (in Degree): ' +str(int(headPose_values[fIndex][3])), (90, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)
        cv2.putText (img, ' "Delta in head yaw (in degree)"  ' + str(abs(int(headPose_values[fIndex][3]) - int(headPose_values[fIndex-1][3]))), (90, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)   
        #cv2.putText(img, 'Normalized Gaze (degree): '+str(float(GazeNormalized_values[fIndex][1])) + ' || '+str(float(GazeNormalized_values[fIndex][3])), (90, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)
        #cv2.putText (img, 'Delta_Normalized Gaze: ' + str("{:.2f}".format( abs(  float(GazeNormalized_values[fIndex][1]) - float(GazeNormalized_values[fIndex-1][1]) ) ))+' || '+ str("{:.2f}".format(abs(float(GazeNormalized_values[fIndex][3]) - float(GazeNormalized_values[fIndex-1][3])))), (90, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)         
        #cv2.putText(img, 'DeNormalized Gaze (degree): '+str(float(GazeDeNormalized_values[fIndex][1])) + ' || '+str(float(GazeDeNormalized_values[fIndex][3])), (90, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)
        #cv2.putText (img, 'Delta in Gaze (Degree): ' + str("{:.2f}".format( abs(  float(GazeDeNormalized_values[fIndex][1]) - float(GazeDeNormalized_values[fIndex-1][1]) ) ))+' || '+ str("{:.2f}".format(abs(float(GazeDeNormalized_values[fIndex][3]) - float(GazeDeNormalized_values[fIndex-1][3])))), (90, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)         
        cv2.putText (img, ' "Delta in gaze yaw (in degree)"  ' +  str("{:.2f}".format(abs(float(GazeDeNormalized_values[fIndex][3]) - float(GazeDeNormalized_values[fIndex-1][3])))), (90, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)         

        cv2.imshow('Frames', img)
        #cv2.imshow("image", thresh)

        #hjsong to put the quit, pause and backward logic q
        nextKey=cv2.waitKey(1) & 0xFF 

        """
        if nextKey == ord ('f') :      #fast twice
            lapTime= lapTime /2
              
        elif  nextKey == ord ('s') :     #slow twice
            lapTime = lapTime * 2
        """    

        if nextKey == ord ('q'):
            break

        elif nextKey == ord('p'):           #pause
            
            nextKey=cv2.waitKey(0) & 0xFF   # contibue, back in the previous frame out of the buffer, and the next frame 
            
            if nextKey == ord ('c') :
                continue



            else :


                bbi=bi+1   # index to buffered index
                while True : 
                    nextKey=cv2.waitKey(0) & 0xFF
                
                    if nextKey == ord ('b')  or nextKey == ord ('n') :
        
                        if nextKey == ord ('b'):
                                bbi=(bbi -1  ) %  buffer_size
                        elif nextKey == ord ('n'):
                                bbi=(bbi + 1 ) %  buffer_size
                        else : pass     

                        iimg=imgBuffer[bbi] 
                        cv2.imshow('Frames', imgBuffer[bbi] )                        
                    elif nextKey == ord ('c') :
                        break
                    else : pass
                        
        else : 
            pass     


    
cap.release()
cv2.destroyAllWindows()



print (f'total # of frame ={fIndex+1}')

 