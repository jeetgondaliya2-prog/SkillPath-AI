 import os
import json
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()


def extract_skills_from_resume(resume_text):

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found")

    model = ChatMistralAI(
        model="mistral-small-latest",
        api_key=api_key
    )

    prompt = f"""
You are a resume skill extraction system.

Analyze the following resume and extract the technical skills
that the candidate actually mentions.

Resume:

{resume_text}

Return ONLY valid JSON in this exact format:

{{
    "skills": [
        "Python",
        "C++",
        "SQL"
    ]
}}

Rules:
- Include programming languages.
- Include frameworks and libraries.
- Include databases.
- Include AI/ML technologies.
- Include developer tools.
- Include concepts such as DSA if mentioned.
- Do not invent skills.
- Do not include soft skills.
"""

    response = model.invoke(prompt)

    content = response.content.strip()

    # Remove markdown code fences if Mistral adds them
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        return {
            "skills": []
        }

    return result
