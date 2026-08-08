from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.learning.resource_recommender import (
    generate_learning_resources
)

router = APIRouter(
    prefix="/api/learning",
    tags=["Learning Resources"]
)


class LearningRequest(BaseModel):

    target_role: str
    missing_skills: list[str]


@router.post("/recommend")
def recommend_learning(request: LearningRequest):

    resources = generate_learning_resources(
        request.target_role,
        request.missing_skills
    )

    return {
        "target_role": request.target_role,
        "missing_skills": request.missing_skills,
        "resources": resources
    }