from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.roadmap.roadmap_generator import (
    generate_roadmap
)

router = APIRouter(
    prefix="/api/roadmap",
    tags=["Roadmap"]
)


class RoadmapRequest(BaseModel):

    target_role: str
    user_skills: list[str]
    missing_skills: list[str]


@router.post("/generate")
def create_roadmap(request: RoadmapRequest):

    roadmap = generate_roadmap(
        request.target_role,
        request.user_skills,
        request.missing_skills
    )

    return {
        "target_role": request.target_role,
        "roadmap": roadmap
    }