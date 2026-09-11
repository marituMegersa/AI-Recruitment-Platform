from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.api.deps import get_db
from app.repositories.domain import RecruitmentSourcingRepository
from app.schemas.search import PaginatedCandidateResponse, CandidateScreenResponse

router = APIRouter(prefix="/search", tags=["Search & Filter"])

@router.get("", response_model=PaginatedCandidateResponse)
async def search_candidates(
    min_score: Optional[float] = Query(None),
    status: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    repo = RecruitmentSourcingRepository(db)
    all_recs = await repo.get_multi(skip=(page - 1) * page_size, limit=page_size)
    items = [
        CandidateScreenResponse(
            candidate_id=r.id,
            candidate_name=r.candidate_name,
            match_score=r.match_score,
            matched_skills=["Python", "FastAPI"],
            screening_status=r.screening_status,
            synthesized_questions=["How do you handle async ORM?"],
            screened_at=r.created_at
        ) for r in all_recs
    ]
    return PaginatedCandidateResponse(
        items=items,
        total=len(items),
        page=page,
        page_size=page_size,
        total_pages=1
    )
