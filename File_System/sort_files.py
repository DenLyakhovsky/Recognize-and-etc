from pathlib import Path
import os
import shutil

"""
Sorts files by directory
"""

# collect the data of the raw_data directory
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
    :param name_dir: parameter that gives the name of the directory
    :param files_iter: give the name of the variable that is iterated by the ITERATION function. Example,
         files_iter(name) = iteration(files.glob('*.pdf'))
    """

    if not Path(f'../File_System/raw_data/{name_dir}/').exists():
        os.mkdir(f'../File_System/raw_data/{name_dir}/')

    if Path(f'raw_data/{name_dir}/').exists():
        for file in files_iter:
            shutil.move(file, f'raw_data/{name_dir}/')


def iteration(body):
    """
    A function that iterates through a list
    :param body: we pass what we want to iterate over
    :return: returns a list of file paths. Example, 'raw_data/exemple.docx'
    """

    list_body = []
    for i in body:
        list_body.append(str(i))
    return list_body


sort_files()
