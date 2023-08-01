import os
import shutil
from pathlib import Path
from imageai.Detection import ObjectDetection
from File_System.sort_files import iteration

"""
Функція, яка розпізнає обʼєкт, який ми задали в 'object'
"""


def object_recognition(object, path_to_photos, path_to_model):
    """
    :param object: Обʼєкт, який хоче знайти. Наприклад, dog, cat
    :param path_to_photos: Шлях до директорія з фотографіями
    :param path_to_model: Шлях до натренованої моделі
    """

    # Дістаємо фото з директорія
    photos = Path(path_to_photos)
    # Перебираємо фото, які закінчуються на формати
    f_jpeg = iteration(photos.glob("*.jpeg"))
    f_jpg = iteration(photos.glob("*.jpg"))
    f_png = iteration(photos.glob("*.png"))

    # Отримуємо шлях до папки, де запускається наш файл python.
    execution_path = os.getcwd()

    # Створюємо новий екземпляр класу, встановлюємо та завантажуємо модель
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, path_to_model))
    detector.loadModel()

    # Якщо немає такої директорія, створюємо
    if not Path(f'../Recognition/{object}_photos_dir').exists():
        os.mkdir(f'../Recognition/{object}_photos_dir/')

    for list_image in (f_jpeg, f_jpg, f_png):
        for image in list_image:
            # Функція 'detectObjectsFromImage' аналізує шлях до фото
            detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, image))

            # Перебираємо detections, і якщо в obj["name"] є обʼєкт, який ми шукаємо - то зберігаємо в директорія
            for obj in detections:
                if object in obj["name"]:
                    source_path = os.path.join(execution_path, image)
                    dest_path = os.path.join(execution_path, f'{object}_photos_dir', f'{image[6:]}')
                    shutil.copyfile(source_path, dest_path)


object_recognition(object='dog', path_to_photos='media',
                   path_to_model="retinanet_resnet50_fpn_coco-eeacb38b.pth")
