import cv2 as cv
import numpy as np
img = cv.imread("./Resources/Photos/cat.jpg")

print(img.shape)

cv.imshow('img', img)
cv.waitKey(0)