from app.domain.recruitment_sourcing.engine import RecruitmentMatchingEngine
from app.domain.recruitment_sourcing.schemas import CandidateScreenRequest, CandidateScreenResponse

class RecruitmentSourcingService:
    @staticmethod
    def screen_candidate(req: CandidateScreenRequest) -> CandidateScreenResponse:
        res = RecruitmentMatchingEngine.match_candidate(
            candidate_name=req.candidate_name,
            skills=req.skills,
            experience_years=req.experience_years
        )
        return CandidateScreenResponse(
            candidate_id=res["candidate_id"],
            candidate_name=req.candidate_name,
            match_score=res["match_score"],
            matched_skills=res["matched_skills"],
            screening_status=res["screening_status"],
            synthesized_questions=res["synthesized_questions"]
        )
