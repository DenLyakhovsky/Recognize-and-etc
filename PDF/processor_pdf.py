from PyPDF2 import PdfReader
import spacy

"""
A function that recognizes named objects and stores them
"""

# Upload model
nlp = spacy.load("en_core_web_sm")

path = "../File_System/raw_data/cv-resume.pdf"


def recognition(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Text processing using spaCy
    doc = nlp(text)

    # Derivation of entities
    with open('../processed_data/ner_results.txt', 'w') as f:
        text = 'Text,Essence\n'
        f.write(text)
        for ent in doc.ents:
            if ent.label_ in ['ORG', 'PERSON', 'GPE']:
                text = f'{ent.text}, {ent.label_}\n'
                f.write(text)

        f.close()


recognition(path)
# File saved in processed_data
