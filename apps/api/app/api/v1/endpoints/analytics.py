from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.repositories.domain import RecruitmentSourcingRepository
from app.schemas.analytics import RecruitmentAnalyticsResponse
from app.services.analytics import RecruitmentAnalyticsService

router = APIRouter(prefix="/analytics", tags=["Talent Sourcing Analytics"])

@router.get("", response_model=RecruitmentAnalyticsResponse)
async def get_analytics(db: AsyncSession = Depends(get_db)):
    repo = RecruitmentSourcingRepository(db)
    service = RecruitmentAnalyticsService(repo)
    return await service.get_sourcing_analytics()
