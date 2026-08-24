# Write your first program
import cv2 as cv
import sys

# Load an image
image = cv.imread("images/test.jpg")

# check if image was loaded successfully
if image is None:
    sys.exit("Could not read the image")

# Diplay the image
cv.imshow("Display Window", image)
k = cv.waitKey(0)

# Save the image
if k == ord("s"):
    cv.imwrite("outputs/test_output.png", image)

