# modules/ats_score.py

def calculate_ats_score(user_profile, required_profile):
    """
    Calculates an ATS-style score for a resume.
    
    Parameters:
        user_profile (dict): Contains user's extracted info:
            {
                "skills": list of skills,
                "projects": list of projects,
                "experience": int (years),
                "education": str/level,
                "keywords": list of keywords
            }
        required_profile (dict): Contains required info for the role/domain:
            {
                "skills": list,
                "projects": list,
                "experience": int (years),
                "education": str/level,
                "keywords": list
            }
            
    Returns:
        ats_score (float): ATS score out of 100
    """
    
    # Define weights
    WEIGHTS = {
        "skills": 30,
        "projects": 20,
        "experience": 20,
        "education": 10,
        "keywords": 20
    }
    
    total_score = 0
    
    # 1️⃣ Skills match
    if required_profile.get("skills"):
        matched_skills = set([s.lower() for s in user_profile.get("skills", [])]) \
                         .intersection(set([s.lower() for s in required_profile["skills"]]))
        skill_score = (len(matched_skills) / len(required_profile["skills"])) * WEIGHTS["skills"]
        total_score += skill_score
    else:
        total_score += WEIGHTS["skills"]  # if no requirement, full marks
    
    # 2️⃣ Projects match
    if required_profile.get("projects"):
        matched_projects = set([p.lower() for p in user_profile.get("projects", [])]) \
                           .intersection(set([p.lower() for p in required_profile["projects"]]))
        project_score = (len(matched_projects) / len(required_profile["projects"])) * WEIGHTS["projects"]
        total_score += project_score
    else:
        total_score += WEIGHTS["projects"]
    
    # 3️⃣ Experience match
    required_exp = required_profile.get("experience", 0)
    user_exp = user_profile.get("experience", 0)
    exp_score = min(user_exp / required_exp, 1.0) * WEIGHTS["experience"] if required_exp > 0 else WEIGHTS["experience"]
    total_score += exp_score
    
    # 4️⃣ Education match (simple level check)
    if required_profile.get("education") and user_profile.get("education"):
        edu_score = WEIGHTS["education"] if required_profile["education"].lower() in user_profile["education"].lower() else 0
    else:
        edu_score = WEIGHTS["education"]  # full marks if not specified
    total_score += edu_score
    
    # 5️⃣ Keywords match
    if required_profile.get("keywords"):
        matched_keywords = set([k.lower() for k in user_profile.get("keywords", [])]) \
                           .intersection(set([k.lower() for k in required_profile["keywords"]]))
        keyword_score = (len(matched_keywords) / len(required_profile["keywords"])) * WEIGHTS["keywords"]
        total_score += keyword_score
    else:
        total_score += WEIGHTS["keywords"]
    
    # Ensure score does not exceed 100
    ats_score = min(total_score, 100)
    return round(ats_score, 2)


# -------------------------
