"""
Advanced Text Cleaning Module for AI Career Agent
-------------------------------------------------

This module performs NLP preprocessing on resume text before
feeding it into the machine learning pipeline.

Processing Steps:
1. Lowercase conversion
2. URL removal
3. Email removal
4. Symbol & number removal
5. Tokenization
6. Stopword removal
7. Lemmatization
8. Whitespace normalization

Output:
Cleaned and normalized text suitable for ML models.
"""

import re
import spacy
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Load small English NLP model
nlp = spacy.load("en_core_web_sm")


def clean_text(text: str) -> str:
    """
    Cleans and normalizes resume text.

    Parameters
    ----------
    text : str
        Raw text extracted from resume.

    Returns
    -------
    str
        Cleaned text ready for TF-IDF vectorization.
    """

    if not isinstance(text, str):
        return ""

    # 1️⃣ Lowercase
    text = text.lower()

    # 2️⃣ Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # 3️⃣ Remove Emails
    text = re.sub(r"\S+@\S+", " ", text)

    # 4️⃣ Remove numbers and symbols
    text = re.sub(r"[^a-z\s]", " ", text)

    # 5️⃣ Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # 6️⃣ NLP processing with spaCy
    doc = nlp(text)

    cleaned_tokens = []

    for token in doc:
        word = token.lemma_.strip()

        if (
            word not in ENGLISH_STOP_WORDS
            and len(word) > 2
        ):
            cleaned_tokens.append(word)

    cleaned_text = " ".join(cleaned_tokens)

    return cleaned_text


# Example test
if __name__ == "__main__":

    sample_text = """
    Python developer with 3+ years experience!!!
    Visit my website https://portfolio.com
    Email me at developer@gmail.com
    """

    print("Before Cleaning:\n")
    print(sample_text)

    print("\nAfter Cleaning:\n")
    print(clean_text(sample_text))