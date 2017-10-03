#!/usr/bin/env python
import cv2
import numpy as np


img=np.zeros((512,512,3),np.uint8)
for i in range(50):
	img=cv2.line(img,(10,10+i*10),(502,10+i*10),(255,i*5,5),5)

for i in range(50):
	img=cv2.line(img,(10+i*10,10),(10+i*10,502),(i*5,255,5),5)
img=cv2.circle(img,(256,256),100,(0,0,255),5)
img=cv2.ellipse(img,(256,256),(100,50),90,0,360,(0,255,0),5)
img=cv2.circle(img,(256,256),256-220,(255,255,255),5)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCv',(10,500),font,4,(255,255,255),5,cv2.LINE_AA)
cv2.imshow('pic',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
