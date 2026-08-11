import cv2
import time

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Store the time when camera opened
start_time = time.time()

while True:
    # Read a frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Calculate elapsed time
    elapsed_time = int(time.time() - start_time)

    # Convert seconds to HH:MM:SS
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60

    timer_text = f"Time: {hours:02}:{minutes:02}:{seconds:02}"

    # Display timer on the frame
    cv2.putText(
        frame,
        timer_text,
        (20, 40),                      # Position
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),                   # Green color
        2
    )

    # Show the frame
    cv2.imshow("Camera", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()