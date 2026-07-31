import cv2
import math

# Create a blank white image
img = 255 * (cv2.UMat(500, 700, cv2.CV_8UC3).get())

drawing = False
center_x, center_y = -1, -1

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    global drawing, center_x, center_y, img

    # When left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        center_x, center_y = x, y

    # When mouse button is released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        # Calculate radius
        radius = int(math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2))

        # Draw circle
        cv2.circle(img, (center_x, center_y), radius, (255, 0, 0), 2)

# Create window
cv2.namedWindow("Draw Circle")

# Connect mouse with function
cv2.setMouseCallback("Draw Circle", draw_circle)

while True:
    cv2.imshow("Draw Circle", img)

    key = cv2.waitKey(1)

    # Press ESC to exit
    if key == 27:
        break

cv2.destroyAllWindows()