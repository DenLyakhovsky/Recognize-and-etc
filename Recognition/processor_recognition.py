import os
import shutil
from pathlib import Path
from imageai.Detection import ObjectDetection
from File_System.sort_files import iteration

"""
A function that recognizes the object we specified in 'object'
"""


def object_recognition(object, path_to_photos, path_to_model):
    """
    :param object: The object to find. For example, dog, cat
    :param path_to_photos: Path to the directory with photos
    :param path_to_model: The path to the trained model
    """

    # We get the photo from the directory
    photos = Path(path_to_photos)
    # We go through photos that end in formats
    f_jpeg = iteration(photos.glob("*.jpeg"))
    f_jpg = iteration(photos.glob("*.jpg"))
    f_png = iteration(photos.glob("*.png"))

    # We get the path to the folder where our python file runs
    execution_path = os.getcwd()

    # Створюємо новий екземпляр класу, встановлюємо та завантажуємо модель
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, path_to_model))
    detector.loadModel()

    # If there is no such directory, create it
    if not Path(f'../Recognition/{object}_photos_dir').exists():
        os.mkdir(f'../Recognition/{object}_photos_dir/')

    for list_image in (f_jpeg, f_jpg, f_png):
        for image in list_image:
            # The 'detectObjectsFromImage' function analyzes the path to the photo
            detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, image))

            # We go through the detections, and if obj["name"] contains the object we are looking for, we save it to the directory
            for obj in detections:
                if object in obj["name"]:
                    source_path = os.path.join(execution_path, image)
                    dest_path = os.path.join(execution_path, f'{object}_photos_dir', f'{image[6:]}')
                    shutil.copyfile(source_path, dest_path)


object_recognition(object='dog', path_to_photos='media',
                   path_to_model="retinanet_resnet50_fpn_coco-eeacb38b.pth")
