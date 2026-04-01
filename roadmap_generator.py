# modules/roadmap_generator.py

import os
import json

# --- Load role -> keywords ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROLE_KEYWORDS_PATH = os.path.join(BASE_DIR, "data", "role_keyword.json")

if not os.path.exists(ROLE_KEYWORDS_PATH):
    raise FileNotFoundError(f"role_keyword.json not found at {ROLE_KEYWORDS_PATH}")

with open(ROLE_KEYWORDS_PATH, "r") as f:
    ROLE_KEYWORDS = json.load(f)


# ------------------------------
# ROLE → DOMAIN mapping (cleaned)
# ------------------------------
ROLE_TO_DOMAIN = {
    "Data Scientist": "AI/Data",
    "Machine Learning Engineer": "AI/Data",
    "Data Analyst": "AI/Data",
    "AI Engineer": "AI/Data",

    "Python Developer": "Software",
    "Web Developer": "Software",
    "Full Stack Developer": "Software",

    "DevOps Engineer": "DevOps",

    "HR Manager": "HR",
    "Marketing Executive": "Marketing",
    "Sales Executive": "Sales",

    "Mechanical Engineer": "Mechanical",
    "Civil Engineer": "Civil",
    "Electrical Engineer": "Electrical",

    "Content Writer": "Creative",
    "UI/UX Designer": "Creative",

    "Fitness Trainer": "Health"
}


# ------------------------------
# 🔥 Get BEST role (IMPORTANT)
# ------------------------------
def get_best_role(user_skills):
    """
    Finds the best matching role based on skill overlap
    """

    user_skills = [s.lower() for s in user_skills]

    best_role = None
    max_match = 0

    for role, role_skills in ROLE_KEYWORDS.items():
        role_skills_lower = [s.lower() for s in role_skills]

        match_count = len(set(user_skills).intersection(role_skills_lower))

        if match_count > max_match:
            max_match = match_count
            best_role = role

    return best_role


# ------------------------------
# 🚀 Roadmap Generator (ROLE BASED)
# ------------------------------
def generate_career_roadmap(user_skills):
    """
    Generate roadmap based on BEST role (not domain)
    """

    if not user_skills:
        return [("Month 1", "Start Learning Basics"),
                ("Month 2", "Build Small Projects"),
                ("Month 3", "Improve Skills"),
                ("Month 4", "Apply for Jobs")]

    # 🔥 Step 1: Get best role
    best_role = get_best_role(user_skills)

    # 🔥 Step 2: Get role-specific skills
    role_skills = ROLE_KEYWORDS.get(best_role, [])

    user_skills = [s.lower() for s in user_skills]
    role_skills_lower = [s.lower() for s in role_skills]

    # 🔥 Step 3: Find missing skills
    missing_skills = [
        skill for skill in role_skills_lower
        if skill not in user_skills
    ]

    # ------------------------------
    # Build roadmap
    # ------------------------------
    roadmap_tasks = []

    # Priority 1: missing skills
    for skill in missing_skills[:4]:
        roadmap_tasks.append(f"Learn {skill.title()}")

    # Priority 2: strengthen known skills
    for skill in role_skills_lower:
        if len(roadmap_tasks) >= 4:
            break
        task = f"Build projects using {skill.title()}"
        if task not in roadmap_tasks:
            roadmap_tasks.append(task)

    # Safety fallback
    while len(roadmap_tasks) < 4:
        roadmap_tasks.append("Build Real-world Projects")

    # ------------------------------
    # Final roadmap
    # ------------------------------
    roadmap = []
    for i in range(4):
        roadmap.append((f"Month {i+1}", roadmap_tasks[i]))

    return roadmap, best_role