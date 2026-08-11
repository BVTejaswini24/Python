import cv2

drawing = False
start_point = (0, 0)
end_point = (0, 0)

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global drawing, start_point, end_point

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)

    # Mouse moving while button is pressed
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)


# Connect camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow("Video")

# Set mouse callback
cv2.setMouseCallback("Video", mouse_callback)

while True:

    # Capture video
    ret, frame = cap.read()

    if not ret:
        print("Camera not working")
        break

    # Draw RED line
    if drawing:
        cv2.line(frame, start_point, end_point, (0, 0, 255), 3)
    else:
        cv2.line(frame, start_point, end_point, (0, 0, 255), 3)

    # Show video
    cv2.imshow("Video", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()