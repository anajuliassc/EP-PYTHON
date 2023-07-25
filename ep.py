import numpy as np
import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()

    img_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
    verde_lower = np.array([])
    verde_upper = np.array([])
    
    mask = cv.inRange(img_hsv, )

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv.destroyAllWindows()
