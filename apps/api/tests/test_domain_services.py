def test_recruitment_sourcing_model_instantiation():
    from app.domain.recruitment_sourcing.models import RecruitmentSourcingRecord
    rec = RecruitmentSourcingRecord(id="REC-TEST-01")
    assert rec.id == "REC-TEST-01"

def test_recruitment_sourcing_schema_validation():
    from app.domain.recruitment_sourcing.schemas import RecruitmentSourcingResponse
    res = RecruitmentSourcingResponse(id="REC-TEST-01", status="COMPLETED", summary="Test", confidence_score=0.99, created_at="2026-09-10T16:00:00Z")
    assert res.status == "COMPLETED"
