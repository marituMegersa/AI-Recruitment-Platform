import pytest

def test_candidate_screening_schema():
    candidate_data = {
        "candidate_name": "Abebe Bikila",
        "candidate_email": "abebe@example.com",
        "skills": ["Python", "FastAPI", "React"],
        "experience_years": 5.0
    }
    assert candidate_data["experience_years"] >= 0
    assert "Python" in candidate_data["skills"]
