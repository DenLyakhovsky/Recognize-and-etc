import os
from pathlib import Path

from PIL import Image, ImageOps, ImageFilter

"""
Uploads photos and processes them
"""


def photo_processing(load_photo):
    if not Path(f'media').exists():
        os.mkdir(f'media')

    image = Image.open(load_photo)

    grayscale(image)
    resized('media/grayscale_output.jpg')
    rotated(image)
    blurred(image)
    mirror(image)


def grayscale(img):
    gray = ImageOps.grayscale(img)
    gray.save('media/grayscale_output.jpg')


def resized(path_to_grayscale_img):
    gray = Image.open(path_to_grayscale_img)

    desired_width = 300
    gray.thumbnail((desired_width, desired_width))
    gray.save("media/resized_output.jpg")


def rotated(img):
    img_rotated = img.rotate(-45)
    img_rotated.save('media/rotated_output.jpg')


def blurred(img):
    img_blur = img.filter(ImageFilter.BLUR)
    img_blur.save('media/blurred_output.jpg')


def mirror(img):
    img_mirror = ImageOps.mirror(img)
    img_mirror.save('media/mirror_output.jpg')


photo_processing('tree.jpg')
