from typing import Dict, Any, List
import uuid

class RecruitmentSourcingService:
    @staticmethod
    def screen_candidate(candidate_name: str, skills: List[str], experience_years: float) -> Dict[str, Any]:
        required_skills = ["Python", "FastAPI", "React", "PyTorch"]
        matched_skills = [s for s in skills if s in required_skills]
        match_score = (len(matched_skills) / len(required_skills)) * 100.0 + (min(experience_years, 5) * 5)
        
        status = "RECOMMENDED_FOR_INTERVIEW" if match_score >= 70.0 else "REVIEW_NEEDED"
        
        return {
            "candidate_id": f"CAND-{uuid.uuid4().hex[:8]}",
            "candidate_name": candidate_name,
            "match_score_percentage": round(match_score, 1),
            "matched_skills": matched_skills,
            "screening_status": status,
            "ai_interview_questions": [
                "Explain your experience building async FastAPI REST backends.",
                "How do you optimize PyTorch model inference for production deployment?"
            ]
        }
