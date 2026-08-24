import cv2 as cv
import numpy as np

# read an image
img = cv.imread('images/car.jpg')

# read as grayscale
gray_img = cv.imread('images/car.jpg', cv.IMREAD_GRAYSCALE)

# display the image
cv.imshow('Image', img)
cv.imshow('gray image', gray_img)
cv.waitKey(0)

cv.destroyAllWindows()
