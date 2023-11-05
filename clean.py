import csv
from tqdm import tqdm
import os

# csv_file_path = os.path.join('.', 'datasets', 'raw_data', 'train', 'labels', 'detections.csv')
csv_file_path = './datasets/raw_data/train/labels/detections.csv'
# 图像文件夹路径
# images_file_path = os.path.join('.', 'train', "data")
images_file_path = './datasets/raw_data/train/data'
images_name = os.listdir(images_file_path)
images_name = [x.split(".")[0] for x in images_name]
# 类别
LabelName = ['/m/01g317', '/m/02p5f1q', '/m/0bt_c3', '/m/020lf']
# 保存标注文件路径
# data_annotation_csv = os.path.join('.', 'train', 'labels', 'clean.csv')
data_annotation_csv_path = './datasets/raw_data/train/labels/clean.csv'
with open(csv_file_path, 'r', encoding='utf-8') as f:
    with open(data_annotation_csv_path, "w", encoding='utf-8') as ff:
        csv_f = csv.reader(f)
        bar = tqdm(csv_f)
        for row in bar:
            if row[0] in images_name and row[2] in LabelName:
                for index in range(len(row)):
                    ff.write(row[index])
                    if (index != (len(row) - 1)):
                        ff.write(",")
                ff.write("\n")
