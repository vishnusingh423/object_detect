import cv2
import numpy as np
import dlib
import time
import cv2
import threading
import math
#importin video 
video = cv2.VideoCapture('cars.mp4')
car_cascade = cv2.CascadeClassifier('file.xml')
#claculation for speed
def estimateSpeed(location1,location2):
    d_pixels=math.sqrt(math.pow(loacation2[0]-location1[0],2)+math.pow(location2[1]-location1[1],2))
    	# ppm = location2[2] / carWidht

    ppm=8.8
    d_meters=d_pixel/ppm
    	#print("d_pixels=" + str(d_pixels), "d_meters=" + str(d_meters))

    fps=18
    speed=d_meters*fps*3.6
    return speed

WIDTH=1280
HEIGHT=720
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)      

    cv2.imshow('video', frame)
    if cv2.waitKey(25) & 0xFF == ord('e'):
        break
video.release()
cv2.destroyAllWindows()
