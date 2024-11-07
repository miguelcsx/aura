# aura/schemas/ai.py

from pydantic import BaseModel


class AskRequest(BaseModel):
    prompt: str
