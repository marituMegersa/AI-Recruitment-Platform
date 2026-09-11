from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.recruitment_sourcing.schemas import CandidateScreenRequest, CandidateScreenResponse
from app.domain.recruitment_sourcing.service import RecruitmentSourcingService

router = APIRouter(prefix="/api/v1/recruitment_sourcing", tags=["AI Talent Sourcing"])

@router.post("/screen", response_model=CandidateScreenResponse, status_code=status.HTTP_201_CREATED)
def screen_candidate(req: CandidateScreenRequest, db: Session = Depends(get_db)):
    return RecruitmentSourcingService.screen_and_store(db, req)

@router.get("/candidates")
def list_candidates(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), db: Session = Depends(get_db)):
    return RecruitmentSourcingService.list_candidates(db, skip=skip, limit=limit)
