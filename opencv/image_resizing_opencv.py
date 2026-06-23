# Image resizing using OpenCV
import cv2
import numpy as np

# read the image using imread function
image = cv2.imread("images/car.jpg")
cv2.imshow("Original Image", image)

# Display the original width and height of the image
h, w, c = image.shape
print(f"Original Height and Width: {h} x {w}")

# Let's downscale the image using new width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)

# Let's upscale the image using new width and height
up_width = 600
up_height = 400
resized_up = cv2.resize(image, (up_width, up_height), interpolation=cv2.INTER_LINEAR)

# display images
cv2.imshow("Resized Down by Defining height and width", resized_down)
cv2.waitKey()

cv2.imshow("Resized Up by Defining height and width", resized_up)
cv2.waitKey()

# press any key to close the windows
cv2.destroyAllWindows()
