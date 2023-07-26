import numpy as np
import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()

    img_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    verde_lower = np.array([25, 50, 70])
    verde_upper = np.array([100, 255, 255])

    mask = cv.inRange(img_hsv, verde_lower, verde_upper)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv.contourArea(contour) > 500:
                g,  r, e, n = cv.boundingRect(contour)
                cv.rectangle(frame, (g,r), (g + e, r + n), (0, 255, 0), 3)

   
    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv.destroyAllWindows()
