import cv2
import numpy as np

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, img = capture.read()
    if not success:
        break

    imgOriginal = img.copy()
    imgHorizontal = cv2.flip(img, 1) 
    imgVertical = cv2.flip(img, 0)  
    imgBoth = cv2.flip(img, -1)  

    row1 = np.hstack((imgOriginal, imgHorizontal))
    row2 = np.hstack((imgVertical, imgBoth))

    fullImage = np.vstack((row1, row2))

    cv2.imshow("Multiple Outputs", fullImage)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
