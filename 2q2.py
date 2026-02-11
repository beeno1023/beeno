import cv2
import numpy as np

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, img = capture.read()
    if not success:
        break

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

    imgCanny = cv2.Canny(imgBlur, 100, 200)

    cv2.imshow("Original", img)
    cv2.imshow("Gaussian Blur", imgBlur)
    cv2.imshow("HSV Color Space", imgHSV)
    cv2.imshow("Canny Edges", imgCanny)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
