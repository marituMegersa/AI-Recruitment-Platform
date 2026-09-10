from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class RecruiterPractitioner(Base):
    __tablename__ = "recruiter_practitioners"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
