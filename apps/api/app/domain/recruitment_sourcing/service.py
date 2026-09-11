from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
import uuid

from app.domain.recruitment_sourcing.models import *
from app.domain.recruitment_sourcing.schemas import *
from app.domain.recruitment_sourcing.engine import *
from app.core.ai_agents import OllamaVLLMProvider, LangGraphAgenticPipeline

class RecruitmentSourcingLangGraphService:
    @staticmethod
    async def evaluate_async(db: AsyncSession, req: Any) -> Any:
        provider = OllamaVLLMProvider()
        pipeline = LangGraphAgenticPipeline(provider)
        agent_res = await pipeline.run_state_graph({"input": str(req)})
        return {"status": "SUCCESS", "agent_state": agent_res}
