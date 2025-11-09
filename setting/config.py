import os
from functools import lru_cache
from dotenv import load_dotenv

@lru_cache()
def get_config():
    return Settings()

def get_ollamaSettings():
    return OllamaSettings()

class Settings():
    app_name:str = "FastAPI"
    author:str = "ShaLin"

    app_mode: str = os.getenv("APP_MODE")
    port:int = int(os.getenv("PORT"))
    reload:bool = bool(os.getenv("RELOAD"))

class OllamaSettings():
    ollama_host:str = os.getenv("OLLAMA_HOST")
    ollama_model:str = os.getenv("OLLAMA_MODEL")