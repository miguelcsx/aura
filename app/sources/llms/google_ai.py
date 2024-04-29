# aura/app/sources/llms/google_ai.py

from langchain_google_genai import ChatGoogleGenerativeAI


class GoogleAI:
    def __init__(self, model_name: str = "gemini-pro"):
        self.llm = ChatGoogleGenerativeAI(model=model_name)

    def generate_text(self, prompt: str) -> str:
        result = self.llm.invoke(prompt)
        return result.content
