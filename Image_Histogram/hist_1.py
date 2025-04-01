import numpy as np
import matplotlib.pyplot as plt

# Given 3×3 grayscale image matrix
image = np.array([
    [50, 100, 150],
    [100, 150, 200],
    [150, 200, 250]
])

# Flatten the image into a 1D array
pixels = image.flatten()

# Plot histogram
plt.hist(pixels, bins=range(0, 256, 50), color='gray', edgecolor='black')

# Labels and title
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.title("Grayscale Image Histogram")

# Define the path for saving the histogram plot
output_path = "./output/hist_1.png"

# Save the histogram plot as an image file
plt.savefig(output_path)

# Show the plot
plt.show()
