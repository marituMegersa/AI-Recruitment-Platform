from fastapi import APIRouter
from app.domain.recruitment_sourcing.service import *

router = APIRouter(prefix="/api/v1/recruitment_sourcing", tags=["AI Recruitment & Talent Sourcing"])

@router.get("/status")
def get_domain_status():
    return {"status": "active", "domain": "AI Recruitment & Talent Sourcing"}
