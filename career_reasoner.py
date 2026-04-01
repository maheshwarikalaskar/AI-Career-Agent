# modules/career_reasoner.py

def reason_career(user_skills, detected_domain):
    """
    Smart career recommendation based on:
    - Detected domain
    - User skills
    Returns:
        List of career suggestions with reasoning
    """

    user_skills = [s.lower() for s in user_skills]

    careers = []

    # ---------------- AI / DATA ----------------
    if detected_domain == "AI/Data":

        if "machine learning" in user_skills or "ml" in user_skills:
            careers.append(("Machine Learning Engineer",
                            "You have ML skills which are core for building predictive models."))

        if "python" in user_skills and "statistics" in user_skills:
            careers.append(("Data Scientist",
                            "Your Python + statistics skills align with data science roles."))

        if "sql" in user_skills or "excel" in user_skills:
            careers.append(("Data Analyst",
                            "Your data handling skills match analysis roles."))

        if "deep learning" in user_skills:
            careers.append(("AI Engineer",
                            "Deep learning is essential for advanced AI systems."))

    # ---------------- WEB DEVELOPMENT ----------------
    elif detected_domain == "Web Development":

        if "html" in user_skills or "css" in user_skills:
            careers.append(("Frontend Developer",
                            "Your UI skills are ideal for frontend development."))

        if "node" in user_skills or "django" in user_skills:
            careers.append(("Backend Developer",
                            "Backend frameworks indicate server-side expertise."))

        if "javascript" in user_skills:
            careers.append(("Full Stack Developer",
                            "JS knowledge helps in both frontend and backend."))

    # ---------------- DEVOPS ----------------
    elif detected_domain == "DevOps":

        if "docker" in user_skills or "kubernetes" in user_skills:
            careers.append(("DevOps Engineer",
                            "Containerization tools are key for DevOps roles."))

        if "aws" in user_skills or "cloud" in user_skills:
            careers.append(("Cloud Engineer",
                            "Cloud platforms are core to scalable infrastructure."))

    # ---------------- DATA ANALYST ----------------
    elif detected_domain == "Data Analyst":

        careers.append(("Data Analyst",
                        "Your skills align well with analyzing and visualizing data."))

        if "tableau" in user_skills or "power bi" in user_skills:
            careers.append(("Business Intelligence Analyst",
                            "Visualization tools indicate BI specialization."))

    # ---------------- CYBER SECURITY ----------------
    elif detected_domain == "Cyber Security":

        careers.append(("Cyber Security Analyst",
                        "Security-focused skills align with threat analysis roles."))

    # ---------------- MANAGEMENT ----------------
    elif detected_domain == "Management":

        careers.append(("Business Analyst",
                        "Your profile aligns with analyzing business processes."))

        careers.append(("Project Manager",
                        "You can manage workflows and teams effectively."))

    # ---------------- CORE ENGINEERING ----------------
    elif detected_domain == "Mechanical":

        careers.append(("Mechanical Engineer",
                        "Your domain knowledge fits core engineering roles."))

    # ---------------- MARKETING ----------------
    elif detected_domain == "Marketing":

        careers.append(("Digital Marketing Specialist",
                        "Marketing domain fits digital promotion roles."))

    # ---------------- HR ----------------
    elif detected_domain == "HR":

        careers.append(("HR Manager",
                        "HR skills align with recruitment and management roles."))

    # ---------------- FALLBACK ----------------
    if not careers:
        careers.append(("General Tech Role",
                        "Explore different domains to find your best fit."))

    return careers