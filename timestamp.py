#import cv2
#import bpy
#import bpy.ops
#import os
#import sys
#import numpy as np

## Load the image


#def write_labels(image_path,text1,text2,name):
#    image = cv2.imread(image_path)

##    # Define the text properties
#    text = f"Position : {text1}, Rotation : {text2}"
#    font = cv2.FONT_HERSHEY_TRIPLEX
#    font_scale = 0.40
#    color = (255, 0, 0)  # Blue color (BGR format)
#    thickness = 1
#    padding = 20  # Padding between text and box

#    # Get the text size
#    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

#    # Calculate the position to place the text (bottom-right corner)
#    x = image.shape[1] - text_width - padding
#    y = image.shape[0] - padding

#    # Calculate the coordinates for the box
#    box_coords = ((x - padding, y - text_height - padding), (x + text_width + padding, y + padding))

#    # Draw the box
#    cv2.rectangle(image, box_coords[0], box_coords[1], color, thickness)

#    # Write the text on the image
#    cv2.putText(image, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)
#    output_folder = "output_folder_write"
#    output_path = os.path.join("D:\\mitacs_blender\\force", output_folder)
#    if not os.path.exists(output_path):
#        os.makedirs(output_path)
#    
#    filepath = os.path.join(output_path,name)
#    cv2.imwrite(filepath, image)

    # Display the image with the text and box
#    cv2.imshow('Image with Text', image)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

import cv2
import numpy as np

# Example 2D points in homogeneous coordinates (adjust these according to your actual points)
points1 = np.array([[100, 150, 1], [200, 250, 1]])
points2 = np.array([[120, 180, 1], [220, 280, 1]])

# Example camera projection matrices (adjust these according to your actual camera matrices)
camera_matrix1 = np.array([[1000, 0, 640, 0], [0, 1000, 480, 0], [0, 0, 1, 0]])
camera_matrix2 = np.array([[1200, 0, 680, 0], [0, 1200, 500, 0], [0, 0, 1, 0]])

# Perform triangulation
point_3d_homogeneous = cv2.triangulatePoints(camera_matrix1, camera_matrix2, points1.T, points2.T)
point_3d_homogeneous /= point_3d_homogeneous[3].astype(np.float32)