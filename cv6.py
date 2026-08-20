import cv2
import numpy as np

# Global variables to track mouse state and position
drawing = False
prev_point = None
canvas = None

def draw_line(event, x, y, flags, param):
    """Mouse callback function to draw on the canvas."""
    global drawing, prev_point, canvas

    # Left click down: start drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        prev_point = (x, y)

    # Mouse move: draw the line if left click is held
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and prev_point is not None:
            # Draw a green line with a thickness of 5 on the CANVAS, not the frame
            cv2.line(canvas, prev_point, (x, y), (0, 255, 0), 5)
            prev_point = (x, y)

    # Left click up: stop drawing
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if prev_point is not None:
            cv2.line(canvas, prev_point, (x, y), (0, 255, 0), 5)
            prev_point = None

def main():
    global canvas

    # Initialize the webcam (0 is usually the default built-in camera)
    cap = cv2.VideoCapture(0)

    # Read the very first frame to get the video's width and height
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not access the webcam.")
        return

    # Create a black canvas matching the exact dimensions of the video frame
    canvas = np.zeros_like(frame)

    # Create the window and attach the mouse callback function to it
    cv2.namedWindow('Live Video Drawing')
    cv2.setMouseCallback('Live Video Drawing', draw_line)

    print("Controls:")
    print(" - Click and drag to draw")
    print(" - Press 'c' to clear the drawing")
    print(" - Press 'q' to quit")

    while True:
        # Read the current live frame
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a natural "mirror" effect
        frame = cv2.flip(frame, 1)

        # OVERLAY THE CANVAS ONTO THE LIVE FRAME
        # 1. Convert canvas to grayscale. Any non-black pixel becomes > 0 (True)
        mask = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY) > 0
        
        # 2. Copy only the drawn pixels from the canvas onto the live frame
        frame[mask] = canvas[mask]

        # Display the combined result
        cv2.imshow('Live Video Drawing', frame)

        # Keyboard controls
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break          # Quit
        elif key == ord('c'):
            # Clear the canvas by resetting it to all zeros (black)
            canvas = np.zeros_like(frame)

    # Clean up and release the camera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()