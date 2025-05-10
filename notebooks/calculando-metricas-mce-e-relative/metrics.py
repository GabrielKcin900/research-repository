import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from utils import load_json, save_json

CORRUPTION_TYPES = {
    'blur': ['defocus_blur', 'guassian_blur', 'glass_blur', 'motion_blur', 'zoom_blur'],
    'digital': ['contrast', 'elastic_transform', 'jpeg_compression', 'pixelate', 'saturate'],
    'noise': ['gaussian_noise', 'impulse_noise', 'shot_noise', 'speckle_noise'],
    'weather': ['brightness', 'fog', 'frost', 'snow' 'spatter']
}
BASE_PATH = '../imagenet-c'


def generate_corruption_error_by_model(model, file_name):
    result = {
        'blur': {},
        'digital': {},
        'noise': {},
        'weather': {}
    }
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function=model.preprocess_input)

    for subject in CORRUPTION_TYPES.keys():
        for corruption_type in range(len(CORRUPTION_TYPES[subject])):
            for severity in range(1, 6):
                corruption_name = CORRUPTION_TYPES[subject][corruption_type]

                generator = datagen.flow_from_directory(
                    f'{BASE_PATH}/{subject}/{corruption_name}/{severity}',
                    target_size=(224, 224),
                    batch_size=64,
                    shuffle=False
                )

                preds = model.predict(generator)
                predicted_classes = np.argmax(preds, axis=1)

                accuracy = accuracy_score(generator.labels, predicted_classes)

                if corruption_name not in result[subject]:
                    result[subject][corruption_name] = {}

                result[subject][corruption_name][severity] = 1 - accuracy

                save_json(f'{file_name}.json', result)


def sum_levels_relative(category_data, baseline_clean_error):
    result = {}
    for key, levels in category_data.items():
        total_sum = 0.
        for corruption_value in levels.values():
            total_sum += corruption_value - baseline_clean_error
        result[key] = total_sum
    return result


def sum_relative_corruption_error(corruption_error_data, baseline_clean_error):
    return {category: sum_levels_relative(corruption_error_data[category], baseline_clean_error) for category in
            corruption_error_data}


def generate_relative_and_corruption_error(sum_ce_model, sum_rel_ce_model, sum_ce_baseline, sum_rel_ce_baseline):
    ce_result = {}
    relative_ce_result = {}
    for key, corruptions in CORRUPTION_TYPES.items():
        for corruption in corruptions:
            corruption_error = sum_ce_model[key][corruption] / sum_ce_baseline[key][corruption]
            relative_corruption_error = sum_rel_ce_model[key][corruption] / sum_rel_ce_baseline[key][corruption]
            ce_result[corruption] = round(corruption_error * 100)
            relative_ce_result[corruption] = round(relative_corruption_error * 100)

    ce_result['mCE'] = round(sum(ce_result.values()) / 15, 1)
    relative_ce_result['Relative mCE'] = round(sum(relative_ce_result.values()) / 15, 1)
    return ce_result, relative_ce_result
