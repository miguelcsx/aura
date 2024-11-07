# aura/api/endpoints/ai.py

from fastapi import (
    APIRouter,
    HTTPException,
)
from aura.services.ai.ai_chat import ChatService
from aura.schemas.ai import AskRequest

router = APIRouter()
chat_service = ChatService()


@router.post("/ai/chat/ask")
def ask(request: AskRequest):
    result = chat_service.ask(request)
    if result is None:
        raise HTTPException(status_code=404, detail="No response from AI")
    return result
