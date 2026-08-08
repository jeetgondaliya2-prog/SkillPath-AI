from pydantic import BaseModel
from typing import List


class StudentProfile(BaseModel):
    name: str
    target_role: str
    skills: List[str]
    education: str
    projects: List[str] = []
    experience: str = "Fresher"