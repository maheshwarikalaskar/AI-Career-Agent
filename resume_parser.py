# modules/resume_parser.py

import pdfplumber
import docx
import io


def extract_pdf(file):
    """
    Extract text from PDF resume
    """
    text = ""

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"

    except Exception as e:
        print("PDF extraction error:", e)

    return text


def extract_docx(file):
    """
    Extract text from DOCX resume
    """
    text = ""

    try:
        document = docx.Document(file)
        for para in document.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print("DOCX extraction error:", e)

    return text


def extract_txt(file):
    """
    Extract text from TXT resume
    """
    try:
        text = file.read().decode("utf-8")
        return text
    except:
        return ""


def parse_resume(uploaded_file):
    """
    Main function used in Streamlit
    Detects file type and extracts resume text
    """

    if uploaded_file is None:
        return ""

    filename = uploaded_file.name.lower()

    # PDF Resume
    if filename.endswith(".pdf"):
        return extract_pdf(uploaded_file)

    # DOCX Resume
    elif filename.endswith(".docx"):
        return extract_docx(uploaded_file)

    # TXT Resume
    elif filename.endswith(".txt"):
        return extract_txt(uploaded_file)

    else:
        raise ValueError("Unsupported file format. Please upload PDF, DOCX, or TXT resume.")