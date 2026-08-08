import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()


def generate_roadmap(target_role, missing_skills):

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found")

    model = ChatMistralAI(
        model="mistral-small-latest",
        api_key=api_key
    )

    prompt = f"""
You are SkillPath AI, an AI career mentor.

A student wants to become a {target_role}.

The student's missing skills are:
{", ".join(missing_skills)}

Create a practical personalized learning roadmap.

Include:

1. Priority order of missing skills
2. 30-day learning roadmap
3. What to learn each week
4. Recommended project ideas
5. Interview preparation topics
6. Daily learning strategy

Keep the answer practical and suitable for a college student.
"""

    response = model.invoke(prompt)

    return response.content