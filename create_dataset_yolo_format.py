import os
import shutil

DATA_OUT_DIR = os.path.abspath(os.path.join('datasets/clean_data'))

for set_ in ['train', 'val', 'test']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_),
                 os.path.join(DATA_OUT_DIR, set_, 'imgs'),
                 os.path.join(DATA_OUT_DIR, set_, 'labels')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.makedirs(dir_, exist_ok=True)

LabelName = ['/m/01g317', '/m/02p5f1q', '/m/0bt_c3', '/m/020lf']

# 使用enumerate函数创建键值对，键是元素，值是索引
alpaca_id_dict = {alpaca_id: index for index, alpaca_id in enumerate(LabelName)}

print(alpaca_id_dict)

train_bboxes_filename = os.path.join('datasets/raw_data/train/labels', 'clean.csv')
# validation_bboxes_filename = os.path.join('datasets/raw_data/validation/labels', 'clean.csv')
# test_bboxes_filename = os.path.join('datasets/raw_data/test/labels', 'clean.csv')

# for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
for j, filename in enumerate([train_bboxes_filename]):
    set_ = ['train', 'val', 'test'][j]
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in LabelName:
                if not os.path.exists(os.path.join(DATA_OUT_DIR, set_, 'imgs', '{}.jpg'.format(id))):
                    shutil.copy(os.path.join("datasets/raw_data", set_, "data", '{}.jpg'.format(id)),
                                os.path.join(DATA_OUT_DIR, set_, 'imgs', '{}.jpg'.format(id)))
                with open(os.path.join(DATA_OUT_DIR, set_, 'labels', '{}.txt'.format(id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1

                    f_ann.write('{} {} {} {} {}\n'.format(alpaca_id_dict[class_name], xc, yc, w, h))
                    print(alpaca_id_dict[class_name])
                    f_ann.close()

            line = f.readline()
