from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.career.career_recommender import (
    recommend_careers
)


router = APIRouter(
    prefix="/api/career",
    tags=["Career Recommendation"]
)


class CareerRequest(BaseModel):

    skills: list[str]


@router.post("/recommend")
def career_recommendation(
    request: CareerRequest
):

    recommendations = recommend_careers(
        request.skills
    )

    return {
        "recommendations": recommendations
    }