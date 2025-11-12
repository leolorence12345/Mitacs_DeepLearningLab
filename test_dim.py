from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import pandas
import cv2
import numpy as np
from PIL import Image

model = YOLO("D:\\mitacs_blender\\segment.pt")
# result = model.predict(source = 'D:\\mitacs_blender\\runs\\detect\\predict2\\crops\\Disk_1\\output_video12.jpg', show = True, save= True, conf = 0.3,hide_labels= True,retina_masks = True,boxes = False)



img ='D:\\mitacs_blender\\runs\\detect\\predict2\\crops\\Disk_1\\output_video128.jpg'
img = cv2.imread(img)
res = model(img)
masks = res[0].masks
polygon = masks.xy[0]
print(polygon)
mask_img = Image.fromarray(polygon,"I")
cv2.imshow('Points', mask_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


