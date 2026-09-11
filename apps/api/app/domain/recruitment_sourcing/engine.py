from typing import Dict, Any, List
import uuid

class RecruitmentMatchingEngine:
    TARGET_SKILLS = ["Python", "FastAPI", "React", "PyTorch", "Docker", "PostgreSQL"]

    @classmethod
    def match_candidate(cls, candidate_name: str, skills: List[str], experience_years: float) -> Dict[str, Any]:
        normalized_skills = [s.strip().title() for s in skills]
        matched = [s for s in cls.TARGET_SKILLS if s.title() in normalized_skills]
        
        skill_score = (len(matched) / len(cls.TARGET_SKILLS)) * 70.0
        exp_score = min(experience_years, 10.0) * 3.0
        total_score = min(round(skill_score + exp_score, 1), 100.0)
        
        status = "RECOMMENDED" if total_score >= 70.0 else "REVIEW_NEEDED"
        
        questions = [
            f"Describe how you apply {matched[0]} in microservice backend architectures." if matched else "How do you structure Python web applications?",
            "Explain your strategy for database transaction management under high concurrence."
        ]
        
        return {
            "candidate_id": f"CAND-{uuid.uuid4().hex[:6].upper()}",
            "match_score": total_score,
            "matched_skills": matched,
            "screening_status": status,
            "synthesized_questions": questions
        }
