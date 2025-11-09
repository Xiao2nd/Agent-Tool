from functools import lru_cache
import ollama
from ollama import ChatResponse
from setting.config import get_ollamaSettings

@lru_cache
def get_ollama_client():
    return OllamaClient()

class OllamaClient:
    def __init__(self):
        settings = get_ollamaSettings()
        self.client = ollama.Client(host=settings.ollama_host)
        self.model = settings.ollama_model

    def chat(self, prompt: str):
        response: ChatResponse = self.client.chat(
            model=self.model,
            messages=[{'role': 'user', 'content': prompt}],
        )
        return response['message']['content']
    
