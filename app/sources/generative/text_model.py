# aura/app/sources/llms/google_ai.py

from langchain_google_genai import ChatGoogleGenerativeAI


class TextModel:

    def __init__(self, model_name: str = "gemini-pro"):
        self.llm = ChatGoogleGenerativeAI(model=model_name)

    def ask(self, question: str) -> str:
        prompt = f"Question: {question}\nAnswer: Be concise and clear."
        result = self.llm.invoke(prompt)
        return result.content

    def explain(self, topic: str) -> str:
        prompt = f"Explain: {topic}\nAnswer: Provide a step by step detailed explanation."
        result = self.llm.invoke(prompt)
        return result.content

    def summarize(self, text: str, type: str) -> str:
        prompt = f"Summarize: {text}\nAnswer: Provide a {type} summary."
        result = self.llm.invoke(prompt)
        return result.content

    def create_mindmap(self, text: str) -> str:
        prompt = f"Create a markdown contextualizing the main ideas to create a mind map for the following text: {text}"
        result = self.llm.invoke(prompt)
        return result.content
