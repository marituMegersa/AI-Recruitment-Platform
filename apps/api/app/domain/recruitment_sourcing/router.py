from fastapi import APIRouter
from app.domain.recruitment_sourcing.schemas import CandidateScreenRequest, CandidateScreenResponse
from app.domain.recruitment_sourcing.service import RecruitmentSourcingService

router = APIRouter(prefix="/api/v1/recruitment_sourcing", tags=["AI Talent Sourcing"])

@router.post("/screen", response_model=CandidateScreenResponse)
def screen_candidate(req: CandidateScreenRequest):
    return RecruitmentSourcingService.screen_candidate(req)

@router.get("/benchmark-skills")
def get_benchmark_skills():
    return {"benchmark_skills": ["Python", "FastAPI", "React", "PyTorch", "Docker", "PostgreSQL"]}
