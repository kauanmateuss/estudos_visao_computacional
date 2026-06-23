import cv2

# read the image in grayscale mode (0)
img_grayscale = cv2.imread("images/test.jpg", 0)
img_original = cv2.imread("images/test.jpg", 1)

# display the image in a window
cv2.imshow("grayscale image", img_grayscale)
cv2.imshow("original image", img_original)

# wait for a key press and close the window
cv2.waitKey(0)

# destroy all windows we created
cv2.destroyAllWindows()

# write the grayscale image to a new file
cv2.imwrite("images/grayscale.jpg", img_grayscale)
cv2.imwrite("images/original.jpg", img_original)