import cv2
import numpy as np

# read the image
image = cv2.imread("./opencv/images/test.jpg")
print(f" Image Shape: {image.shape}")
cv2.imshow("Original", image)

# crop an image using array slicing
cropped_image = image[100: 400, 100:800]

# display cropped image
cv2.imshow("cropped image", cropped_image)

# save the cropped image to a new file
cv2.imwrite("./opencv/images/cropped_image.jpg", cropped_image)

cv2.waitKey()
cv2.destroyAllWindows()