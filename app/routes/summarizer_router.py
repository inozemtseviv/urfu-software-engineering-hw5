from fastapi import APIRouter

from app.models import SummarizerRequest, SummarizerResponse
from app.services.base_summarizer_service import BaseSummarizerService


def get_summarizer_router(summarizer: BaseSummarizerService):
    router = APIRouter()

    @router.post("/summarize")
    def summarize(request: SummarizerRequest) -> SummarizerResponse:
        return SummarizerResponse(text=summarizer.summarize(request.text))

    return router
