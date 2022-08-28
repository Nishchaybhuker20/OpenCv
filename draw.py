import cv2 as cv
import numpy as np

blank = np.zeros((512,512,3), dtype='uint8')
cv.imshow('Blank', blank)


#cv.rectangle(blank, (0,0), (255,250), thickness = 2)
#cv.imshow('Rectanle', blank)
#cv.imshow('Green', blank)

#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green',blank)

#cv.rectangle(blank,(0,0),(255,250), thickness = 2)

#cv.imshow('Rectanle', blank)

cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255),
thickness = -1)

cv.putText(blank, 'Hello', (215,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text', blank)

cv.waitKey(0)