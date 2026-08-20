import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the video horizontally
    flipped = cv2.flip(frame, 1)

    cv2.imshow("Original Video - Press Q", frame)
    cv2.imshow("Flipped Video", flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()