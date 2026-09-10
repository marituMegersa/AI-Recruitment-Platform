from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import List
from app.domain.recruitment_sourcing.service import RecruitmentSourcingService

router = APIRouter(prefix="/api/v1/recruitment_sourcing", tags=["Recruitment Sourcing"])

class ScreeningInput(BaseModel):
    candidate_name: str
    skills: List[str]
    experience_years: float

@router.post("/screen", status_code=status.HTTP_200_OK)
def screen_candidate(data: ScreeningInput):
    return RecruitmentSourcingService.screen_candidate(data.candidate_name, data.skills, data.experience_years)
