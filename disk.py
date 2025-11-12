from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
# import cv2

model = YOLO("D:\\mitacs_blender\\best_2.pt")
model.predict('D:\\mitacs_blender\\force\output_folder_test\\FRONT_view16.png', save=True, imgsz=320, conf=0.3,show= True)
