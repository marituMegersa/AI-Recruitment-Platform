from pydantic import BaseModel, Field
from typing import Dict, List

class RecruitmentAnalyticsResponse(BaseModel):
    total_candidates_screened: int = Field(..., example=450)
    recommended_count: int = Field(..., example=180)
    review_needed_count: int = Field(..., example=270)
    average_match_score: float = Field(..., example=78.4)
    top_in_demand_skills: Dict[str, int] = Field(..., example={"Python": 410, "FastAPI": 320, "React": 290})
