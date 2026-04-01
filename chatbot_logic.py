# utilis/chatbot_logic.py
import json
import os
import streamlit as st

# 🔹 Fix path to role_keyword.json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # one level up from utils/
ROLE_KEYWORDS_PATH = os.path.join(BASE_DIR, "data", "role_keyword.json")

# Load skill map
if not os.path.exists(ROLE_KEYWORDS_PATH):
    raise FileNotFoundError(f"role_keyword.json not found at {ROLE_KEYWORDS_PATH}")

with open(ROLE_KEYWORDS_PATH, "r") as f:
    SKILL_MAP = json.load(f)


def chatbot_response(question):
    q = question.lower()

    # Skill advice
    if "skill" in q and "data scientist" in q:
        skills = SKILL_MAP.get("Data Science", [])
        return f"To become a Data Scientist you should learn: {', '.join(skills)}"

    if "skill" in q and "python developer" in q:
        skills = SKILL_MAP.get("Python Developer", [])
        return f"For Python Developer roles you should learn: {', '.join(skills)}"

    # Resume improvement
    if "improve my resume" in q or "resume tips" in q:
        return (
            "Here are some tips to improve your resume:\n\n"
            "• Add measurable achievements\n"
            "• Highlight relevant technical skills\n"
            "• Include real projects\n"
            "• Keep formatting clean and professional\n"
            "• Tailor your resume to the job role"
        )

    # Projects suggestion
    if "project" in q and "data science" in q:
        return (
            "Good Data Science projects include:\n\n"
            "• House Price Prediction\n"
            "• Customer Churn Prediction\n"
            "• Resume Classification (like your project)\n"
            "• Movie Recommendation System"
        )

    if "project" in q and "ai" in q:
        return (
            "Good AI projects:\n\n"
            "• Chatbot using NLP\n"
            "• Image Classification\n"
            "• AI Resume Analyzer\n"
            "• Fake News Detection"
        )

    return "I'm here to help with career advice, skills, projects, or resume tips!"


# ------------------------------
# Streamlit integration helpers
# ------------------------------
def init_chat(path_key, meta):
    """Initialize chat for a given path if empty"""
    if path_key not in st.session_state.messages:
        st.session_state.messages[path_key] = [
            {"role": "assistant", "content": f"How can I help you with your {meta[path_key]['title']} today?"}
        ]


def handle_input(path_key):
    """Display chat messages, handle input, and update session state"""
    for m in st.session_state.messages[path_key]:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages[path_key].append({"role": "user", "content": prompt})
        response = chatbot_response(prompt)
        st.session_state.messages[path_key].append({"role": "assistant", "content": response})
        st.rerun()