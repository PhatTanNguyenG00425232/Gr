import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('ATU.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert BGR image to RGB for correct color display with matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

nrows = 2
ncols = 1
# Plot the original and grayscale images
plt.subplot(nrows, ncols, 1), plt.imshow(img_rgb)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols, 2), plt.imshow(gray, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])


plt.tight_layout()
plt.show()
