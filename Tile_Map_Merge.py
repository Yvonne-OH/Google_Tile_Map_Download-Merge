import os
from tqdm import tqdm
import cv2
import numpy as np

def merge_images_in_folders(current_directory):
    folders = [folder for folder in os.listdir(current_directory) if
               os.path.isdir(os.path.join(current_directory, folder))]

    folders.sort(key=folder_sort_key, reverse=True)

    result = None

    for i, folder in enumerate(tqdm(folders, desc="Merging Map: "), start=1):

        folder_path = os.path.join(current_directory, folder)
        file_names = os.listdir(folder_path)
        file_names = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.png')]
        sorted_file_names = sorted(file_names, key=lambda x: int(os.path.splitext(x)[0]))

        row_array = []

        for file_name in sorted_file_names:
            image = cv2.imread(os.path.join(folder_path, file_name))
            row_array.append(image)
            # print(file_name)

        col_array = np.hstack(row_array)

        if i == 1:
            result = col_array
        else:
            result = np.concatenate((result, col_array), axis=0)

    return result


def folder_sort_key(folder):
    try:
        return int(folder)
    except ValueError:
        return float('inf')
    # %%