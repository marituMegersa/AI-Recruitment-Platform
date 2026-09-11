from sqlalchemy.orm import Session
from typing import List, Optional
import uuid
from app.domain.recruitment_sourcing.models import RecruitmentSourcingRecord
from app.domain.recruitment_sourcing.schemas import CandidateScreenRequest, CandidateScreenResponse
from app.domain.recruitment_sourcing.engine import RecruitmentMatchingEngine

class RecruitmentSourcingService:
    @staticmethod
    def screen_and_store(db: Session, req: CandidateScreenRequest) -> CandidateScreenResponse:
        res = RecruitmentMatchingEngine.match_candidate(
            candidate_name=req.candidate_name,
            skills=req.skills,
            experience_years=req.experience_years
        )
        
        db_obj = RecruitmentSourcingRecord(
            id=res["candidate_id"],
            job_title="Senior AI Systems Engineer",
            candidate_name=req.candidate_name,
            candidate_email=req.candidate_email,
            match_score=res["match_score"],
            skills_json={"skills": req.skills, "matched": res["matched_skills"]},
            screening_status=res["screening_status"]
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return CandidateScreenResponse(
            candidate_id=db_obj.id,
            candidate_name=db_obj.candidate_name,
            match_score=db_obj.match_score,
            matched_skills=res["matched_skills"],
            screening_status=db_obj.screening_status,
            synthesized_questions=res["synthesized_questions"],
            screened_at=db_obj.created_at
        )

    @staticmethod
    def list_candidates(db: Session, skip: int = 0, limit: int = 50) -> List[RecruitmentSourcingRecord]:
        return db.query(RecruitmentSourcingRecord).offset(skip).limit(limit).all()
