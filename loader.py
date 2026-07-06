import os
import PyPDF2
import pandas as pd
from docx import Document


def load_pdf(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    return text


def load_docx(file_path):
    doc = Document(file_path)

    text = "\n".join([para.text for para in doc.paragraphs])

    return text


def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def load_csv(file_path):
    df = pd.read_csv(file_path)

    return df.to_string(index=False)


def extract_text(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return load_pdf(file_path)

    elif extension == ".docx":
        return load_docx(file_path)

    elif extension == ".txt":
        return load_txt(file_path)

    elif extension == ".csv":
        return load_csv(file_path)

    else:
        raise ValueError("Unsupported file format")