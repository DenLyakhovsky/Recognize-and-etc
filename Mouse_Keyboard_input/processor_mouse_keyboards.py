import pyautogui
from pyautogui import moveTo, click, write
import webbrowser

"""
Функція, яка автоматизує процес завантаження 'data_analysis_report.docx' i 'ner_results.xlsx' на хмарну платформу
"""

pyautogui.PAUSE = 1


def uploads_files():
    # Відкриваємо сторінку
    url = 'https://drive.google.com'
    webbrowser.open(url)

    moveTo(80, 180, duration=3)
    click()

    moveTo(130, 245, duration=1)
    click()

    moveTo(1000, 260, duration=1)
    click()
    write('processed_data', interval=0.25)

    moveTo(520, 420, duration=1)
    click()
    moveTo(1050, 625, duration=1)
    click()


uploads_files()
