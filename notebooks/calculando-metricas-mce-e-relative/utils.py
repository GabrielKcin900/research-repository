import pandas as pd
import os
import json


def generate_data_with_labels(image_dir):
    all_file_paths = []
    labels = []

    all_folds = os.listdir(image_dir)
    for fold in all_folds:
        fold_path = os.path.join(image_dir, fold)
        all_files_in_fold = os.listdir(fold_path)
        for file in all_files_in_fold:
            file_path = os.path.join(fold_path, file)
            all_file_paths.append(file_path)
            labels.append(fold)
    return pd.DataFrame(data={"file_path": all_file_paths, "labels": labels})


def save_json(output_name, data_dict):
    with open(output_name, 'w') as file:
        json.dump(data_dict, file)
    print("File save with success!")


def load_json(output_name):
    with open(output_name, 'r') as file:
        data_dict = json.load(file)
    print("File loaded with success!")

    return data_dict
