from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.domain import CandidateScreenResponse

class CandidateSearchQuery(BaseModel):
    min_score: Optional[float] = Field(None, example=70.0)
    status: Optional[str] = Field(None, example="RECOMMENDED")
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=100)

class PaginatedCandidateResponse(BaseModel):
    items: List[CandidateScreenResponse]
    total: int
    page: int
    page_size: int
    total_pages: int

# Search & Pagination Criteria Filter
