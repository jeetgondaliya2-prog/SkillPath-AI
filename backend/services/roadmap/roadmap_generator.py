import os
from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv() 

client = Mistral(
    api_key=os.getenv("MISTRAL_API_KEY")
)


def generate_roadmap(
    target_role,
    user_skills,
    missing_skills
):

    prompt = f"""
You are an expert career mentor.

Create a personalized learning roadmap for a student.

Target Career:
{target_role}

Current Skills:
{", ".join(user_skills)}

Missing Skills:
{", ".join(missing_skills)}

Create a practical roadmap.

Include:

1. Learning order
2. Important topics for each skill
3. Recommended duration
4. One project after learning the major skills
5. DSA/interview preparation
6. Final job preparation

Keep the roadmap realistic for a student.

Format the answer with clear headings,
weeks/phases and bullet points.
"""

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
