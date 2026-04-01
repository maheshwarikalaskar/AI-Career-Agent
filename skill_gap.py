# modules/skill_gap.py

def detect_skill_gap(user_skills, required_skills):
    """
    Compares user's skills with required skills and returns:
    - missing_skills
    - matched_skills
    """

    # ✅ Safety check
    if not user_skills or not required_skills:
        return [], []

    # ✅ Normalize (lowercase + strip)
    user_skills_set = set(s.lower().strip() for s in user_skills)
    required_skills_set = set(s.lower().strip() for s in required_skills)

    # ✅ Find matches & gaps
    matched_skills = list(user_skills_set.intersection(required_skills_set))
    missing_skills = list(required_skills_set - user_skills_set)

    # ✅ Sort for clean UI
    matched_skills.sort()
    missing_skills.sort()

    return missing_skills, matched_skills