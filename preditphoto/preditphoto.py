import cv2
from ultralytics import YOLO
import os

# 模型路径
model_path = os.path.join('..', 'runs', 'detect', 'train11', 'weights', 'last.pt')
# 图像路径
image_path = "./bus.jpg"  # 替换为要检测的图像路径

# 加载YOLO模型
model = YOLO(model_path)

# 加载图像
image = cv2.imread(image_path)

# 进行目标检测
results = model(image)[0]

# 设置置信度阈值
threshold = 0.5

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        # 绘制框
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

        # 获取物体标签
        label = results.names[int(class_id)].upper()

        # 计算文本绘制位置，位于框的下方，确保不超出图像边界
        text_x = int(x1)
        text_y = int(y2)   # 调整文本与框的垂直距离

        # 绘制文本背景
        cv2.rectangle(image, (text_x, text_y - 30), (text_x + len(label) * 17, text_y), (0, 255, 0), -1)

        # 绘制文本
        cv2.putText(image, label, (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

# 显示检测结果
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
