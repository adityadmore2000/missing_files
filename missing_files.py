# set difference method
import os

root_dir = input("Enter path to directory: ")

images = set()
labels = set()

for file in os.listdir(root_dir):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        # if image_label_pair.get(file) is None:
        images.add(file.split('.')[0])
    else:
        labels.add(file.split('.')[0])

are_images_missing = labels.difference(images)
are_labels_missing = images.difference(labels)

if are_images_missing:
    print("images missing: ",are_images_missing)
    # for file in are_images_missing:
    #     if file!='classes.txt':
    #         file_to_remove = os.path.join(root_dir, f"{file}.json")
    #         if os.path.exists(file_to_remove):
    #             os.remove(file_to_remove)
if are_labels_missing:
    print("labels_missing: ",are_labels_missing)
    # for file_in_are_labels_missing in are_labels_missing:
    #     for file in os.listdir(root_dir):
    #         if file.startswith(file_in_are_labels_missing):
    #             os.remove(os.path.join(root_dir,file))




# import os
#
# root_dir = input("Enter path to directory: ")
# for file in os.listdir(root_dir):
#     if file.lower().endswith(('.jpg','.jpeg','.png')):
#         if not os.path.exists(os.path.join(root_dir,f"{file.split('.')[0]}.txt")):
#             print(file," has no .json file ")