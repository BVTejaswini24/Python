import cv2

# Open the default camera (0 = first webcam)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Display the frame
    cv2.imshow("Camera", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()