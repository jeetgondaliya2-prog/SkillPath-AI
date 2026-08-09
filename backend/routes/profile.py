from fastapi import APIRouter, UploadFile, File, Form

from backend.schemas.profile import StudentProfile
from backend.services.skill_analyzer import analyze_skills
from backend.services.ai_service import generate_roadmap
from backend.services.resume_parser import extract_resume_text
from backend.services.resume_analyzer import extract_skills_from_resume


router = APIRouter()


@router.post("/analyze")
def analyze_profile(profile: StudentProfile):

    result = analyze_skills(
        profile.target_role,
        profile.skills
    )

    if "error" in result:
        return result

    roadmap = generate_roadmap(
        profile.target_role,
        result["missing_skills"]
    )

    return {
        "student": profile.name,
        "analysis": result,
        "roadmap": roadmap
    }
@router.post("/resume")
async def analyze_resume(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are supported."
        }

    # Extract text from PDF
    text = extract_resume_text(file.file)

    # Extract skills using Mistral
    skills_result = extract_skills_from_resume(text)

    return {
        "filename": file.filename,
        "skills": skills_result["skills"]
    }
@router.post("/resume/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    target_role: str = Form(...)
):

    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are supported."
        }

    # 1. Extract text from resume
    resume_text = extract_resume_text(file.file)

    if not resume_text.strip():
        return {
            "error": "Could not extract text from resume."
        }

    # 2. Extract skills using Mistral
    skills_result = extract_skills_from_resume(resume_text)

    resume_skills = skills_result.get("skills", [])

    # 3. Analyze skill gap
    analysis = analyze_skills(
        target_role,
        resume_skills
    )

    if "error" in analysis:
        return analysis

    # 4. Generate personalized roadmap
    roadmap = generate_roadmap(
        target_role,
        analysis["missing_skills"]
    )

    # 5. Return complete result
    return {
        "filename": file.filename,
        "target_role": target_role,
        "resume_skills": resume_skills,
        "analysis": analysis,
        "roadmap": roadmap
    }
