import cv2
import numpy as np

# Reading the image
image = cv2.imread("images/image-15.png", 0)
cv2.imshow("Original Image", image)
cv2.waitKey()

# Get the height and width of the image
height, width = image.shape[:2]

# get tx and ty value for translation
tx, ty = (width / 4, height / 4)

# create the translation matrix
translate_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)

translated_image = cv2.warpAffine(src=image, M=translate_matrix, dsize=(width, height))

cv2.imshow("Translated Image", translated_image)
cv2.waitKey()

cv2.destroyAllWindows()

# print(image.shape)
