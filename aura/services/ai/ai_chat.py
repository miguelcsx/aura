# services/ai/ai_chat.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from aura.services.ai.config import config


class ChatService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=config.MODEL_NAME,
            google_api_key=config.GOOGLE_API_KEY,
            temperature=0,
            max_tokens=None,
            max_retries=2,
        )

    def ask(self, question: str) -> str:
        function_prompt: str = """
        Provide a direct, clear, and concise response to this {question} based on verified general knowledge. 
        Avoid unnecessary elaboration or ambiguity. Limit the answer to a single paragraph, 
        focusing only on the most relevant and accurate information.
        """

        prompt = PromptTemplate.from_template(template=function_prompt)

        prompt_formatted = prompt.format(
            question=question,
        )

        result = self.llm.invoke(prompt_formatted)

        return result.content
