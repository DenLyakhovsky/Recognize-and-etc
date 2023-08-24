from docx import Document
from docx.shared import Inches
from visualization_data import read_xlsx, get_text

"""
Функція, яка створює повний звіт із файлів 'data_analysis_repost.docx' i 'processed_data/processed_data.xlsx'
"""


def data_report():
    doc = Document()

    # Заголовок
    doc.add_heading('Привіт, це аналітика', level=4)

    # Вставлення короткої інформації про файл sample1.docx
    docx_file = get_text('../File_System/raw_data/sample1.docx')
    doc.add_paragraph(f'Коротко про цей файл. \n{docx_file[0]}. {docx_file[1]}')

    # Виведення таблиці
    doc.add_heading('Таблиця всіх присутніх', level=2)

    # Отримання даних з файлу processed_data.xlsx
    data_excel = read_xlsx()

    # Створення таблиці
    table = doc.add_table(rows=len(data_excel) + 1, cols=3)

    # Заповнення заголовків стовпців
    table.cell(0, 0).text = 'ID'
    table.cell(0, 1).text = 'Імʼя'
    table.cell(0, 2).text = 'Прізвище'

    # Заповнення таблиці даними
    for i, item in enumerate(data_excel):
        id = item.get('id')
        first_name = item.get('first_name')
        last_name = item.get('last_name')
        table.cell(i + 1, 0).text = str(id)
        table.cell(i + 1, 1).text = first_name
        table.cell(i + 1, 2).text = last_name

    # Видалення контенту (тексту) з комірок
    table.cell(1, 0).text = ''
    table.cell(1, 1).text = ''
    table.cell(1, 2).text = ''

    # Виведення зображення
    doc.add_paragraph('\nЦей графік дасть зрозуміти щось')
    doc.add_picture('media/plot.png', width=Inches(5.0))

    # Збереження
    doc.save('data_analysis_repost.docx')


data_report()
