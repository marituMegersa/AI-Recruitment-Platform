from sqlalchemy import Column, String, DateTime, Float, JSON, ForeignKey
import datetime
from app.core.database import Base

class CompanyOrganization(Base):
    __tablename__ = "company_organizations"
    id = Column(String, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class RecruitmentSourcingRecord(Base):
    __tablename__ = "recruitment_sourcing_records"
    id = Column(String, primary_key=True, index=True)
    job_title = Column(String, nullable=False, index=True)
    candidate_name = Column(String, nullable=False)
    candidate_email = Column(String, nullable=False)
    match_score = Column(Float, default=0.0)
    skills_json = Column(JSON, nullable=False)
    screening_status = Column(String, default="SHORTLISTED")
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)
