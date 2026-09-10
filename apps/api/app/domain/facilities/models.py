from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class RecruitmentOffice(Base):
    __tablename__ = "recruitment_offices"

    id = Column(String, primary_key=True, index=True)
    office_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
