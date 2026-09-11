from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import uuid
import datetime

from app.models.domain import RecruitmentSourcingRecord
from app.repositories.domain import RecruitmentSourcingRepository
from app.schemas.domain import CandidateScreenRequest, CandidateScreenResponse

class RecruitmentSourcingService:
    def __init__(self, repo: RecruitmentSourcingRepository):
        self.repo = repo

    async def screen_candidate_profile(self, req: CandidateScreenRequest) -> CandidateScreenResponse:
        required = ["Python", "FastAPI", "React", "PyTorch", "Docker"]
        matched = [s for s in req.skills if s in required]
        score = min(round((len(matched) / len(required)) * 70 + min(req.experience_years, 10) * 3, 1), 100.0)
        status_val = "RECOMMENDED" if score >= 70.0 else "REVIEW_NEEDED"

        record_id = f"CAND-{uuid.uuid4().hex[:6].upper()}"
        db_obj = RecruitmentSourcingRecord(
            id=record_id,
            job_title="Senior AI Engineer",
            candidate_name=req.candidate_name,
            candidate_email=req.candidate_email,
            match_score=score,
            skills_json={"skills": req.skills, "matched": matched},
            screening_status=status_val,
            created_at=datetime.datetime.utcnow()
        )
        saved = await self.repo.create(db_obj)

        return CandidateScreenResponse(
            candidate_id=saved.id,
            candidate_name=saved.candidate_name,
            match_score=saved.match_score,
            matched_skills=matched,
            screening_status=saved.screening_status,
            synthesized_questions=[
                f"Explain how you design FastAPI async dependencies for {req.candidate_name}.",
                "How do you manage vector search embeddings in Elasticsearch?"
            ],
            screened_at=saved.created_at or datetime.datetime.utcnow()
        )

    async def list_candidates(self, skip: int = 0, limit: int = 50) -> List[RecruitmentSourcingRecord]:
        return await self.repo.get_multi(skip=skip, limit=limit)

# Business logic & AI engine orchestrator
