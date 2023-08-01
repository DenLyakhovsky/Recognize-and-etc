import pandas as pd

"""
Скрипт, який зчитує оброблені дана Excel і обʼєднує
"""

xlsx = pd.read_excel('../processed_data/processed_data.xlsx', sheet_name=1)
txt = pd.read_csv('../processed_data/ner_results.txt')


def final_report(xlsx_file, txt_file):
    df_xlsx = pd.DataFrame(xlsx_file)
    del df_xlsx[0]
    df_txt = pd.DataFrame(txt_file)

    # Обʼєднуємо дані
    data = pd.merge(df_xlsx[['Last Name', 'Age', 'Date', 'Id']], df_txt[['Essence']], left_index=True,
                    right_index=True, how='outer')

    data.to_excel('../processed_data/final_report.xlsx')


final_report(xlsx, txt)
