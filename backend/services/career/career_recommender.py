import json
import os


def load_careers():

    base_dir = os.path.dirname( 
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        )
    )

    file_path = os.path.join(
        base_dir,
        "data",
        "career_roles.json"
    )

    with open(file_path, "r") as file:
        return json.load(file)


def recommend_careers(user_skills):

    careers = load_careers()

    # Convert user skills to lowercase
    user_skills = {
        skill.strip().lower()
        for skill in user_skills
    }

    recommendations = []

    for career in careers:

        required_skills = {
            skill.lower()
            for skill in career["skills"]
        }

        matched = (
            user_skills & required_skills
        )

        missing = (
            required_skills - user_skills
        )

        score = (
            len(matched) /
            len(required_skills)
        ) * 100

        recommendations.append({
            "role": career["role"],
            "match_percentage": round(score),
            "matched_skills": sorted(matched),
            "missing_skills": sorted(missing)
        })

    # Highest match first
    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations
