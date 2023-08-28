import pyautogui
from pyautogui import moveTo, click, write
import webbrowser

"""
A function that automates the process of uploading 'data_analysis_report.docx' and 'ner_results.xlsx' to the cloud platform
"""

pyautogui.PAUSE = 1


def uploads_files():
    # Open browser
    url = 'https://drive.google.com'
    webbrowser.open(url)

    moveTo(80, 180, duration=10)
    click()

    moveTo(130, 245, duration=4)
    click()

    moveTo(1000, 260, duration=2)
    click()
    write('processed_data', interval=0.25)

    moveTo(522, 556, duration=2)
    click()
    moveTo(1050, 625, duration=1)
    click()


uploads_files()
