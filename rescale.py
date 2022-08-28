import cv2 as cv

#img = cv.imread('images/1.jpg')
#cv.imshow('meow', img)

def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('videos/1.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.14)
    cv.imshow('Videp', frame)
    cv.imshow('video', frame_resized)
    cv.imshow('video',changeRes)
    cv.imshow('video', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.waitKey(0)