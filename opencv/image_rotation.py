import cv2

# Reading the image
image = cv2.imread("images/image-15.png")
cv2.imshow("Original Image", image)
cv2.waitKey()

# print(image.shape)

# Get the height and width of the image
height, width = image.shape[:2]

# get the center of the image from height and width
center = (width/2, height/2)

# print(center)

# Defining the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=1)

# rotating the image using warpAffine
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

# Display the rotated image
cv2.imshow("Rotated image", rotated_image)
cv2.waitKey()

cv2.destroyAllWindows()