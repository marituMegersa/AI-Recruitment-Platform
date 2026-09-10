from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.recruitment_sourcing.models import RecruitmentSourcingRecord
from app.domain.recruitment_sourcing.schemas import RecruitmentSourcingRequest

class RecruitmentSourcingService:
    @staticmethod
    def process_encounter(db: Session, data: RecruitmentSourcingRequest) -> RecruitmentSourcingRecord:
        rec_id = f"REC-{uuid.uuid4().hex[:8]}"
        db_obj = RecruitmentSourcingRecord(
            id=rec_id,
            created_at=datetime.datetime.utcnow()
        )
        return db_obj
