# modules/domain_detector.py

import json
from collections import defaultdict
import os

# -------------------------
# 1️⃣ Load role_keywords.json safely
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROLE_KEYWORDS_PATH = os.path.join(BASE_DIR, "data", "role_keyword.json")

with open(ROLE_KEYWORDS_PATH, "r") as f:
    role_keyword = json.load(f)

# -------------------------
# 2️⃣ Automatically infer domains
# -------------------------
ROLE_TO_DOMAIN = {}

for role in role_keyword.keys():

    role_lower = role.lower()

    if "data" in role_lower or "python" in role_lower or "ml" in role_lower or "science" in role_lower:
        ROLE_TO_DOMAIN[role] = "AI/Data"

    elif "web" in role_lower or "html" in role_lower or "ui" in role_lower or "frontend" in role_lower:
        ROLE_TO_DOMAIN[role] = "Web Development"

    elif "devops" in role_lower or "docker" in role_lower or "aws" in role_lower:
        ROLE_TO_DOMAIN[role] = "DevOps"

    elif "analyst" in role_lower or "sql" in role_lower or "excel" in role_lower or "tableau" in role_lower:
        ROLE_TO_DOMAIN[role] = "Data Analyst"

    elif "hr" in role_lower:
        ROLE_TO_DOMAIN[role] = "HR"

    elif "marketing" in role_lower:
        ROLE_TO_DOMAIN[role] = "Marketing"

    elif "mechanical" in role_lower:
        ROLE_TO_DOMAIN[role] = "Mechanical"

    elif "advocate" in role_lower or "law" in role_lower:
        ROLE_TO_DOMAIN[role] = "Legal"

    elif "arts" in role_lower:
        ROLE_TO_DOMAIN[role] = "Creative/Arts"

    elif "sales" in role_lower:
        ROLE_TO_DOMAIN[role] = "Sales"

    elif "fitness" in role_lower or "health" in role_lower or "nutrition" in role_lower or "gym" in role_lower:
        ROLE_TO_DOMAIN[role] = "Health/Fitness"

    else:
        ROLE_TO_DOMAIN[role] = "General/Unknown"


# -------------------------
# 3️⃣ Build domain_skills dictionary
# -------------------------
domain_skills = defaultdict(set)

for role, keywords in role_keyword.items():

    domain = ROLE_TO_DOMAIN.get(role, "General/Unknown")

    for k in keywords:
        domain_skills[domain].add(k.lower())


# Convert sets → lists
for d in domain_skills:
    domain_skills[d] = list(domain_skills[d])


# -------------------------
# 4️⃣ Domain Detection Function
# -------------------------
def detect_domain(user_skills):

    """
    Detects the most probable domain based on user's skills.
    """

    # Safety check
    if not user_skills:
        return "General/Unknown", []

    user_skills_set = set([s.lower().strip() for s in user_skills])

    best_domain = "General/Unknown"
    max_overlap = 0
    matched_skills = []

    for domain, skills in domain_skills.items():

        overlap = user_skills_set.intersection(set(skills))

        if len(overlap) > max_overlap:

            max_overlap = len(overlap)
            best_domain = domain
            matched_skills = list(overlap)

    return best_domain, matched_skills