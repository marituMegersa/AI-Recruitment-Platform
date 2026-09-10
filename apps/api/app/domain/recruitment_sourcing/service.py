from typing import Dict, Any, List
import uuid

class RecruitmentSourcingService:
    @staticmethod
    def screen_candidate(candidate_name: str, skills: List[str], experience_years: float) -> Dict[str, Any]:
        required_skills = ["Python", "FastAPI", "React", "PyTorch"]
        matched = [s for s in skills if s in required_skills]
        score = (len(matched) / len(required_skills)) * 100.0 + (min(experience_years, 5) * 5)
        return {
            "candidate_id": f"CAND-{uuid.uuid4().hex[:8]}",
            "candidate_name": candidate_name,
            "match_score_percentage": round(score, 1),
            "matched_skills": matched,
            "screening_status": "RECOMMENDED_FOR_INTERVIEW" if score >= 70.0 else "REVIEW_NEEDED"
        }
