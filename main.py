from ultralytics import YOLO
# Create a new YOLO model from scratch
# model = YOLO('yolov8n.yaml')
# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
results = model.train(data="config.yaml", epochs=500)  # train the model
