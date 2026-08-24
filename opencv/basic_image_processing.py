import cv2 as cv

# read the image
image = cv.imread("images/image-15.png")

# Convert to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# apply Gaussian Blur
blurred = cv.GaussianBlur(gray_image, (5, 5), 0)

# Detect edges using Canny
edges = cv.Canny(blurred, 50, 150)

# Display all results
cv.imshow("Original", image)
cv.imshow("Grayscale", gray_image)
cv.imshow("Edges", edges)

cv.waitKey(0)
cv.destroyAllWindows()