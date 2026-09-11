from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.deps import get_db
from app.schemas.domain import CandidateScreenRequest, CandidateScreenResponse
from app.repositories.domain import RecruitmentSourcingRepository
from app.services.domain import RecruitmentSourcingService

router = APIRouter(prefix="/recruitment", tags=["AI Talent Sourcing"])

def get_service(db: AsyncSession = Depends(get_db)) -> RecruitmentSourcingService:
    repo = RecruitmentSourcingRepository(db)
    return RecruitmentSourcingService(repo)

@router.post("/screen", response_model=CandidateScreenResponse, status_code=status.HTTP_201_CREATED)
async def screen_candidate(req: CandidateScreenRequest, service: RecruitmentSourcingService = Depends(get_service)):
    return await service.screen_candidate_profile(req)

@router.get("/candidates")
async def list_candidates(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), service: RecruitmentSourcingService = Depends(get_service)):
    return await service.list_candidates(skip=skip, limit=limit)
