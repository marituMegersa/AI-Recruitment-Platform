import pytest
from app.services.domain import RecruitmentSourcingService
from app.repositories.domain import RecruitmentSourcingRepository
from app.schemas.domain import CandidateScreenRequest

class MockSession:
    def add(self, obj): pass
    async def commit(self): pass
    async def refresh(self, obj): pass

@pytest.mark.asyncio
async def test_candidate_screening_recommended():
    service = RecruitmentSourcingService(RecruitmentSourcingRepository(MockSession()))
    req = CandidateScreenRequest(
        candidate_name="Abebe Bikila",
        candidate_email="abebe@example.com",
        skills=["Python", "FastAPI", "React", "PyTorch", "Docker"],
        experience_years=5.0
    )
    res = await service.screen_candidate_profile(req)
    assert res.match_score >= 70.0
    assert res.screening_status == "RECOMMENDED"
    assert len(res.matched_skills) == 5

@pytest.mark.asyncio
async def test_candidate_screening_review_needed():
    service = RecruitmentSourcingService(RecruitmentSourcingRepository(MockSession()))
    req = CandidateScreenRequest(
        candidate_name="Junior Dev",
        candidate_email="junior@example.com",
        skills=["Python"],
        experience_years=0.5
    )
    res = await service.screen_candidate_profile(req)
    assert res.match_score < 70.0
    assert res.screening_status == "REVIEW_NEEDED"
