import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
 
client = Mistral(
    api_key=os.getenv("MISTRAL_API_KEY")
)


def generate_learning_resources(
    target_role,
    missing_skills
):

    skills = ", ".join(missing_skills)

    prompt = f"""
You are an expert career mentor.

Target Career:
{target_role}

Missing Skills:
{skills}

Create a practical learning resource plan for the missing skills.

For every skill provide:

1. What to learn
2. Important topics
3. Practice activities
4. A small project idea
5. Approximate learning priority

Keep the answer beginner-friendly and practical.

Do NOT provide fake URLs.
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
