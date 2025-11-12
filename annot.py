import cv2
import numpy as np

#def draw_bounding_boxes(image_path, centers, box_width, box_height):
#    # Load the image
#    image = cv2.imread(image_path)

#    # Iterate over the center points
#    for center in centers:
#        # Calculate the top-left corner coordinates
#        x = int(center[0] - box_width / 2)
#        y = int(center[1] - box_height / 2)

#        # Calculate the bottom-right corner coordinates
#        x2 = int(center[0] + box_width / 2)
#        y2 = int(center[1] + box_height / 2)

#        # Draw the bounding box on the image
#        cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)

#    # Display the annotated image
#    cv2.imshow("Annotated Image", image)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

#    # Save the annotated image
#    annotated_image_path = "annotated_" + image_path
#    cv2.imwrite(annotated_image_path, image)
#    print("Annotated image saved as:", annotated_image_path)

## Example usage
#image_path = "D:\\mitacs_blender\\force\\output_folder\\FRONT_view0.png"
#centers = [(100, 100), (200, 200), (300, 300)]
#box_width = 50
#box_height = 50

#draw_bounding_boxes(image_path, centers, box_width, box_height)
def create_label_file(image_path, centers, box_width, box_height, class_labels, label_file_path):
    image = cv2.imread(image_path)
    image_height, image_width, _ = image.shape
    with open(label_file_path, 'w') as f:
        for i, center in enumerate(centers):
            class_label = class_labels[i]
            x = center[0] / image_width  # Normalize x-coordinate
            y = center[1] / image_height  # Normalize y-coordinate
            width = box_width / image_width  # Normalize width
            height = box_height / image_height  # Normalize height

            label_line = f"{class_label} {x} {y} {width} {height}\n"
            f.write(label_line)

    print("Label file created:", label_file_path)

def draw_bounding_boxes(image_path, centers, box_width, box_height, class_labels, label_file_path):
    # Load the image
    image = cv2.imread(image_path)


    # Iterate over the center points
    for i, center in enumerate(centers):
        # Calculate the top-left corner coordinates

        x = int(center[0] - box_width / 2)
        y = int(center[1] - box_height / 2)

        # Calculate the bottom-right corner coordinates
        x2 = int(center[0] + box_width / 2)
        y2 = int(center[1] + box_height / 2)

        # Draw the bounding box on the image
        cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)

        # Add the class label
        label = class_labels[i]
        cv2.putText(image, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the annotated image
    cv2.imshow("Annotated Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the annotated image
    annotated_image_path = "annotated_" + image_path
    cv2.imwrite(annotated_image_path, image)
    print("Annotated image saved as:", annotated_image_path)

    # Create the label file
    image_height, image_width, _ = image.shape
    create_label_file(image_path, centers, box_width, box_height, class_labels, label_file_path)

# Example usage
image_path = "D:\\mitacs_blender\\force\\output_folder\\SIDE_view.png"
rotation_matrix = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])  # Rotation matrix for coordinate transformation

centers = [(10.436275780200958,15.08374559879303)]
box_width = 20
box_height = 20
class_labels = ["car", "person", "dog"]
label_file_path = "D:\\mitacs_blender\\force\\output_folder\\FRONT_view.txt"
draw_bounding_boxes(image_path, centers, box_width, box_height, class_labels, label_file_path)

