from matplotlib import pyplot as plt
from docx import Document
from Excel.processor_excel import read_all_xlsx_data


def get_text(filename):
    document = Document(filename)

    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)
    return full_text


def read_xlsx():
    xlsx_data = read_all_xlsx_data('../processed_data/processed_data.xlsx')
    data = []
    for v in xlsx_data.values():

        for item in v:
            data.append({'first_name': item[1], 'last_name': item[2], 'id': item[-1]})

    return data


def create_plot():
    # Дані для графіка
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 12, 9]

    # Створення графіка
    plt.plot(x, y)
    plt.xlabel('X-позиція')
    plt.ylabel('Y-позиція')
    plt.title('Графік даних')

    plt.savefig('media/plot.png')
