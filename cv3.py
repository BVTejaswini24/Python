import cv2
import numpy as np

# Create a blank image (300 pixels high, 600 pixels wide)
img = np.zeros((300, 600, 3), dtype=np.uint8)

# Draw vertical color stripes
img[:, 0:100] = (255, 0, 0)      # Blue
img[:, 100:200] = (0, 255, 0)    # Green
img[:, 200:300] = (0, 0, 255)    # Red
img[:, 300:400] = (255, 255, 0)  # Cyan
img[:, 400:500] = (0, 255, 255)  # Yellow
img[:, 500:600] = (255, 0, 255)  # Magenta

cv2.imshow("Color Stripes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()