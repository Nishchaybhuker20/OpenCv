import cv2 as cv

img = cv.imread('images/1.jpg')

#cv.imshow('Mine', img)
#color grey
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#blur functions
#blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#finding edge in a images
canny = cv.Canny(img, 125,175)
cv.imshow('edge',canny)

dilate = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('dilate', dilate)

#eroding
eroded = cv.erode(dilate, (3,3), iterations = 1)
cv.imshow('erode', eroded)

#resize
#resized = cv.resize(img, (500,500), interplation = cv.INTER_AREA)
#cv.imshow('resize',resized)

#cropped
cropped = img[200:100, 200:300]
cv.imshow('cropped',cropped)

cv.waitKey(0)