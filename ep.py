import numpy as np
import cv2 as cv

from limits import limits


green = [0, 255, 0]
cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()

    image_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    limit_min, limit_max = limits(color=green)

    mask = cv.inRange(image_hsv, limit_min, limit_max)

    cv.imshow('frame', mask)

    if cv.waitKey(1) == ord('q'):
        break
cam.release()
cv.destroyAllWindows()
