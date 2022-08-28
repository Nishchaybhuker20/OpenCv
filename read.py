import cv2 as cv

#img = cv.imread('images/1.jpg')

#cv.imshow('Cat', img)
capture = cv.VideoCapture('videos/1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Videp', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
#cv.waitKey(0)