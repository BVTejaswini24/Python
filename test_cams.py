import cv2

print("Scanning for available cameras...")
for i in range(5):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"Camera index {i} is available and grabbing frames.")
        else:
            print(f"Camera index {i} is available but cannot grab frames.")
        cap.release()
print("Scan complete.")
