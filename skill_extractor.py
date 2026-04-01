import json
import re
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Load role-keyword mapping
with open("data/role_keyword.json", "r") as f:
    ROLE_KEYWORDS = json.load(f)

# Flatten all keywords into a unique skill set
ALL_SKILLS = set()
for keywords in ROLE_KEYWORDS.values():
    ALL_SKILLS.update([k.lower() for k in keywords])

# Words that should NOT be considered as skills
STOPWORDS = {
    "resume","education","year","experience","team","project",
    "analysis","technology","computer","nagpur","iit","application",
    "engineer","engineering","skill","build","design","resume","education","year","experience","team","project",
    "analysis","technology","computer","nagpur","iit","application",
    "engineer","engineering","skill","build","design",
    "com","net","reduce","data","database"
}


def extract_skills(resume_text):
    """
    Hybrid skill extraction using:
    1. Rule-based keyword matching
    2. SpaCy NLP token detection
    """

    resume_text_lower = resume_text.lower()

    detected_skills = set()

    # -------- RULE BASED MATCHING --------
    for skill in ALL_SKILLS:

        if skill in STOPWORDS:
            continue

        pattern = r'\b' + re.escape(skill).replace("\\ ", r"\s+") + r'\b'

        if re.search(pattern, resume_text_lower):
            detected_skills.add(skill.title())

    # -------- SPACY NLP EXTRACTION --------
    doc = nlp(resume_text)

    for token in doc:

        word = token.text.lower()

        if token.pos_ in ["NOUN", "PROPN"]:

            if word in ALL_SKILLS and word not in STOPWORDS:
                detected_skills.add(word.title())

    return sorted(list(detected_skills))


def extract_role_skills(resume_text):
    """
    Returns a mapping of roles to number of matched keywords in resume.
    """

    resume_text_lower = resume_text.lower()
    role_skill_match = {}

    for role, keywords in ROLE_KEYWORDS.items():

        matched = []

        for kw in keywords:

            pattern = r'\b' + re.escape(kw.lower()).replace("\\ ", r"\s+") + r'\b'

            if re.search(pattern, resume_text_lower):
                matched.append(kw.title())

        if matched:
            role_skill_match[role] = sorted(matched)

    return role_skill_match


# Example usage
if __name__ == "__main__":

    sample_text = """
    Python developer with experience in Machine Learning, Tableau, and analytics.
    Worked on deep learning projects and Matlab simulations.
    """

    print("Detected Skills:", extract_skills(sample_text))
    print("Role-wise Skills:", extract_role_skills(sample_text))