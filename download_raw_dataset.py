import fiftyone.zoo

# classes = ["Coffee cup", "Book", "Computer mouse", "Person"]
# for i in range(len(classes)):
#     item = classes[i]
#     print(item)
#     dataset = fiftyone.zoo.load_zoo_dataset(
#         "open-images-v7",
#         splits=["train"],
#         label_types=["detections"],
#         classes=[item],
#         max_samples=1000,
#         dataset_dir="./datasets/raw_data",
#     )

# dataset = fiftyone.zoo.load_zoo_dataset(
#         "open-images-v7",
#         splits=["train"],
#         label_types=["detections"],
#         classes=["Coffee cup"],
#         max_samples=1000,
#         dataset_dir="./datasets/raw_data",
#     )
# dataset1 = fiftyone.zoo.load_zoo_dataset(
#         "open-images-v7",
#         splits=["validation"],
#         label_types=["detections"],
#         classes=["Coffee cup"],
#         max_samples=100,
#         dataset_dir="./datasets/raw_data",
#     )
#
# dataset2 = fiftyone.zoo.load_zoo_dataset(
#         "open-images-v7",
#         splits=["train"],
#         label_types=["detections"],
#         classes=["Book"],
#         max_samples=1000,
#         dataset_dir="./datasets/raw_data",
#     )
# dataset3 = fiftyone.zoo.load_zoo_dataset(
#         "open-images-v7",
#         splits=["validation"],
#         label_types=["detections"],
#         classes=["Book"],
#         max_samples=100,
#         dataset_dir="./datasets/raw_data",
#     )

dataset4 = fiftyone.zoo.load_zoo_dataset(
        "open-images-v7",
        splits=["train"],
        label_types=["detections"],
        classes=["Computer mouse"],
        max_samples=1000,
        dataset_dir="./datasets/raw_data",
    )
dataset5 = fiftyone.zoo.load_zoo_dataset(
        "open-images-v7",
        splits=["validation"],
        label_types=["detections"],
        classes=["Computer mouse"],
        max_samples=100,
        dataset_dir="./datasets/raw_data",
    )

# dataset6 = fiftyone.zoo.load_zoo_dataset(
#         "open-images-v7",
#         splits=["train"],
#         label_types=["detections"],
#         classes=["Person"],
#         max_samples=1000,
#         dataset_dir="./datasets/raw_data",
#     )
# dataset7 = fiftyone.zoo.load_zoo_dataset(
#         "open-images-v7",
#         splits=["validation"],
#         label_types=["detections"],
#         classes=["Person"],
#         max_samples=100,
#         dataset_dir="./datasets/raw_data",
#     )