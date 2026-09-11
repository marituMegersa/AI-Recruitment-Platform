from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class CandidateScreenRequest(BaseModel):
    candidate_name: str = Field(..., example="Abebe Bikila")
    candidate_email: str = Field(..., example="abebe@example.com")
    skills: List[str] = Field(..., example=["Python", "FastAPI", "React", "Docker"])
    experience_years: float = Field(..., ge=0, le=50, example=4.5)

class CandidateScreenResponse(BaseModel):
    candidate_id: str
    candidate_name: str
    match_score: float
    matched_skills: List[str]
    screening_status: str
    synthesized_questions: List[str]
    screened_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
