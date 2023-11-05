from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np


model = YOLO("/home/ps/Code/ROS/robot_ws/src/vision/yolo/scripts/yolov8x.pt")  # load a pretrained model (recommended for training)
# 识别整个文件夹
# results = model.predict(source="./YoloPicture/YoloPicture/inside", save=True) # Display preds. Accepts all YOLO predict arguments

#识别一张图片
# im1 = Image.open("bus.jpg")
im1 = cv2.imread("bus.jpg")

results = model.predict(source=im1)[0]
threshold = 0.1

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        # 绘制框
        cv2.rectangle(im1, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)

        # 获取物体标签
        label = results.names[int(class_id)].upper()

        # 绘制文本
        cv2.putText(im1, label, (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imwrite("output.jpg", im1)


