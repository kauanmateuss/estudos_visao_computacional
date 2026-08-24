import cv2 as cv

# open webcam (0 = default Camera)
cap = cv.VideoCapture(0)

# Or open a video file
# cap = cv.VideoCapture("video.mp4")

while True:
    # read frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to Grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display
    cv.imshow("WebCam", gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()