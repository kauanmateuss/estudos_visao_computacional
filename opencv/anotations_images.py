import cv2

# read image
image = cv2.imread("images/dog.jpg")

cv2.imshow("Original Image", image)
esc = cv2.waitKey(0)

# print(image.shape)

# Print error message if image is null
if image is None:
    print("Could not read image")

# Draw line on image
imageLine = image.copy()
pointA = (10, 80)
pointB = (450, 10)

# For Draw a circle
imageCircle = image.copy()
circle_center = (415, 190)
radius = 100

# For draw a Rectangle
imageRec = image.copy()
pointX = (300, 115)
pointY = (475, 225)

# Draw a circle using the circle() function
cv2.circle(imageCircle, circle_center, radius, (0,0,255), thickness=-1, lineType=cv2.LINE_AA)

# Draw a line on the image
cv2.line(imageLine, pointA, pointB, (255,255,0), thickness=3, lineType=cv2.LINE_AA)

cv2.rectangle(imageRec, pointX, pointY, (255, 0, 0), thickness=3, lineType=cv2.LINE_8)

# Display the image Line
cv2.imshow("Image Line", imageLine)
cv2.imshow("Image circle", imageCircle)
cv2.imshow("Image Rect", imageRec)

cv2.waitKey(0)
