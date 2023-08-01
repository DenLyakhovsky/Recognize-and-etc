from pathlib import Path
import os
import shutil

"""
Сортує файли по директоріях
"""

# збираємо дані директорії raw_data
files = Path('raw_data')


def sort_files():
    file_pdf = iteration(files.glob('*.pdf'))
    verification(name_dir='pdf_data', files_iter=file_pdf)

    file_excel = iteration(files.glob('*.xlsx'))
    verification(name_dir='excel_data', files_iter=file_excel)

    file_word = iteration(files.glob('*.docx'))
    verification(name_dir='word_data', files_iter=file_word)


def verification(name_dir, files_iter):
    """
    :param name_dir: параметр, який дає назву директорії
    :param files_iter: даємо назву перемінної, яка проітерована функцією ITERATION. Приклад,
        files_iter(імʼя) = iteration(files.glob('*.pdf'))
    """

    if not Path(f'../File_System/raw_data/{name_dir}/').exists():
        os.mkdir(f'../File_System/raw_data/{name_dir}/')

    if Path(f'raw_data/{name_dir}/').exists():
        for file in files_iter:
            shutil.move(file, f'raw_data/{name_dir}/')


def iteration(body):
    """
    Функція, яка перебирає список
    :param body: передаємо те, що хочемо перебрати
    :return: повертає список є шлях до файлу. Приклад, 'raw_data/exemple.docx'
    """

    list_body = []
    for i in body:
        list_body.append(str(i))
    return list_body


sort_files()
