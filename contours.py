import cv2 as cv


#contour is used in object detection and using face detection

 
img = cv.imread('images/2.png')

cv.imshow('Cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


canny = cv.Canny(gray, 100, 200)
cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)