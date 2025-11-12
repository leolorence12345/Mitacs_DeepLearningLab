import numpy as np
import cv2

# Example camera calibration matrix K
focal_length_x = 1000.0  # Example focal length in pixels (for X-axis)
focal_length_y = 1000.0  # Example focal length in pixels (for Y-axis)
principal_point_x = 640.0  # Example principal point in pixels (X-coordinate)
principal_point_y = 480.0  # Example principal point in pixels (Y-coordinate)

K = np.array([[focal_length_x, 0, principal_point_x],
              [0, focal_length_y, principal_point_y],
              [0, 0, 1]])

# Example keypoints in image 1 (2D coordinates)
keypoints_image1 = np.array([[320.0, 240.0],   # Keypoint 1
                             [400.0, 300.0],   # Keypoint 2
                             [280.0, 360.0],   # Keypoint 3
                             [500.0, 250.0]])  # Keypoint 4

# Example keypoints in image 2 (corresponding 2D coordinates)
keypoints_image2 = np.array([[330.0, 235.0],   # Corresponding Keypoint 1
                             [420.0, 310.0],   # Corresponding Keypoint 2
                             [290.0, 370.0],   # Corresponding Keypoint 3
                             [510.0, 245.0]])  # Corresponding Keypoint 4


# Corresponding 3D points (set to zero since we don't have them)
object_points = np.zeros((len(keypoints_image1), 3), dtype=np.float32)

# Perform Perspective-n-Point (PnP) pose estimation
_, rvec, tvec, _ = cv2.solvePnPRansac(object_points, keypoints_image2, K, None)

# rvec: Rotation vector
# tvec: Translation vector

# Convert the rotation vector to a rotation matrix
R, _ = cv2.Rodrigues(rvec)

# The rotation matrix R and translation vector t represent the object's pose
# R is a 3x3 rotation matrix, and t is a 3x1 translation vector.

# You can now use R and t to transform the object's local coordinate system to the global/world coordinate system.
print(rvec,R,tvec)
