from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class CompanyOrganization(Base):
    __tablename__ = "company_organizations"

    id = Column(String, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    offices = relationship("RecruitmentOffice", back_populates="company", cascade="all, delete-orphan")
