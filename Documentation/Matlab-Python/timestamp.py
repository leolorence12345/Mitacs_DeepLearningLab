import cv2
import bpy
import bpy.ops
import os
import sys
import numpy as np

# Load the image


def write_labels(image_path,text1,text2,name):
    image = cv2.imread(image_path)

#    # Define the text properties
    text = f"Position : {text1}, Rotation : {text2}"
    font = cv2.FONT_HERSHEY_TRIPLEX
    font_scale = 0.40
    color = (255, 0, 0)  # Blue color (BGR format)
    thickness = 1
    padding = 20  # Padding between text and box

    # Get the text size
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

    # Calculate the position to place the text (bottom-right corner)
    x = image.shape[1] - text_width - padding
    y = image.shape[0] - padding

    # Calculate the coordinates for the box
    box_coords = ((x - padding, y - text_height - padding), (x + text_width + padding, y + padding))

    # Draw the box
    cv2.rectangle(image, box_coords[0], box_coords[1], color, thickness)

    # Write the text on the image
    cv2.putText(image, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)
    output_folder = "output_folder_write"
    output_path = os.path.join("D:\\mitacs_blender\\force", output_folder)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    filepath = os.path.join(output_path,name)
    cv2.imwrite(filepath, image)

    # Display the image with the text and box
#    cv2.imshow('Image with Text', image)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

