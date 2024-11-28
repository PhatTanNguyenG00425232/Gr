import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('ATU.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert BGR image to RGB for correct color display with matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define different kernel sizes for the blurring
kernel_sizes = [(3, 3),  (13, 13)]


nrows = 2
ncols = 2
# Plot the original and grayscale images
plt.subplot(nrows, ncols, 1), plt.imshow(img_rgb)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols, 2), plt.imshow(gray, cmap='gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

# Apply Gaussian Blur with different kernel sizes and display the results
for i, size in enumerate(kernel_sizes, start=3):
    blurred_img = cv2.GaussianBlur(gray, size, 0)
    blurred_rgb = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB)
    
    plt.subplot(nrows, ncols, i)
    plt.imshow(blurred_rgb)
    plt.title(f'Gaussian Blur {size[0]}x{size[1]}')
    plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
