from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class RecruitmentOffice(Base):
    __tablename__ = "recruitment_offices"

    id = Column(String, primary_key=True, index=True)
    office_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    company_id = Column(String, ForeignKey("company_organizations.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    company = relationship("CompanyOrganization", back_populates="offices")
    recruiters = relationship("RecruiterPractitioner", back_populates="office", cascade="all, delete-orphan")
