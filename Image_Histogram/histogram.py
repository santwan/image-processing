"""
==========================================================
Grayscale Image Histogram Plotter using OpenCV & Matplotlib
==========================================================

Description:
------------
This script reads a grayscale image, computes its histogram, 
and then plots and saves the histogram as an image.

Steps:
1. Load the grayscale image from the specified path.
2. Compute the histogram of the image.
3. Plot the histogram using Matplotlib.
4. Save the histogram as an output image.

Author: [Your Name]  
Date: [YYYY-MM-DD]  
"""

# Import necessary libraries
import cv2  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for plotting

# Define the path to the input image
image_path = "./images/sample1.jpg"  # Change this to your image path

# Load the image in grayscale mode
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found at", image_path)  # Print an error if file is missing
    exit()  # Exit the script if image loading fails

# Flatten the image into a 1D array and compute the histogram
histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

# Create a figure for the histogram
plt.figure()

# Set title and labels for the plot
plt.title("Grayscale Image Histogram")  # Title of the histogram
plt.xlabel("Pixel Intensity")  # X-axis: Intensity values (0-255)
plt.ylabel("Frequency")  # Y-axis: Number of pixels per intensity

# Set the x-axis range from 0 to 255 (full grayscale range)
plt.xlim([0, 255])

# Plot the histogram as a line graph in black color
plt.plot(histogram, color='black')

# Define the path for saving the histogram plot
output_path = "./output/histogram.png"

# Save the histogram plot as an image file
plt.savefig(output_path)

# Display the histogram
plt.show()

# Print confirmation message
print(f"Histogram saved successfully at: {output_path}")
