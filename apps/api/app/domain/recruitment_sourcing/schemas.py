from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class RecruitmentSourcingRequest(BaseModel):

    job_title: str
    candidate_name: str
    candidate_email: str
    skills: List[str] = []
    experience_years: float


class RecruitmentSourcingResponse(BaseModel):
    id: str
    status: str = "COMPLETED"
    summary: str
    confidence_score: float = 0.98
    created_at: datetime

    class Config:
        from_attributes = True
