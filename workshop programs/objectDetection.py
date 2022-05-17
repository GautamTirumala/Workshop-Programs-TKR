import cv2 as cv
import numpy as np

cap= cv.VideoCapture(0)

while(1):
    hbj , frame = cap.read()
    cv.imshow('input',frame)

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.imshow('hsv video', hsv)


    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])

    mask = cv.inRange(hsv,lower_blue,upper_blue)

    res = cv.bitwise_and(frame,frame,mask = mask)

    cv.imshow('mask', mask)
    cv.imshow('bakegrouns -',res)
    
    if cv.waitKey(1) & 0xFF ==ord('s'):
     break


cv.destroyAllWindows()