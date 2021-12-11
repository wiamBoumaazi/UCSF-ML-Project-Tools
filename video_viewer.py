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

cap = cv2.VideoCapture('/Users/wiamboumaazi/Desktop/UCSF-ML-Project-Tools/AGportrait28withsidelight.mov')
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
        cv2.putText(img, ' "fIndex" ' +str(fIndex), (90, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 128), 2)        
    
        cv2.imshow('Frames', img)
        
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

 