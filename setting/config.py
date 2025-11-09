import os
from functools import lru_cache
from dotenv import load_dotenv

@lru_cache()
def get_config():
    load_dotenv( f".env.{os.getenv('APP_MODE')}")
    return Settings()

class Settings():
    app_name:str = "FastAPI"
    author:str = "ShaLin"

    app_mode: str = os.getenv("APP_MODE")
    port:int = int(os.getenv("PORT"))
    reload:bool = bool(os.getenv("RELOAD"))