import json
from pathlib import Path


# SkillPath/
# ├── data/
# │   └── roles.json
# └── backend/
#     └── services/
#         └── skill_analyzer.py

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROLES_FILE = BASE_DIR / "data" / "roles.json"


def load_roles():

    with open(ROLES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_skills(target_role, student_skills):

    roles = load_roles()

    role = target_role.lower().replace(" ", "_")

    if role not in roles:
        return {
            "error": f"Role '{target_role}' not found"
        }

    required_skills = roles[role]["required_skills"]

    student_skills_lower = [
        skill.lower()
        for skill in student_skills
    ]

    matched = []
    missing = []

    for skill in required_skills:

        if skill.lower() in student_skills_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    score = round(
        len(matched) / len(required_skills) * 100
    )

    return {
        "target_role": target_role,
        "matched_skills": matched,
        "missing_skills": missing,
        "readiness_score": score
    }