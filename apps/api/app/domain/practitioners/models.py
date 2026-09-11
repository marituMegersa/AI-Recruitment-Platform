from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class RecruiterPractitioner(Base):
    __tablename__ = "recruiter_practitioners"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    office_id = Column(String, ForeignKey("recruitment_offices.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    office = relationship("RecruitmentOffice", back_populates="recruiters")
