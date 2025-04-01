import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "../images/sample.jpg"  # Ensure image is in the 'images' folder
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
    exit()

# Compute histogram
histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

# Plot histogram
plt.figure()
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 255])
plt.plot(histogram, color='black')

# Save histogram
plt.savefig("../output/histogram.png")
plt.show()
