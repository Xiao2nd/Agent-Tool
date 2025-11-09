from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "HelloWorld"}


from setting.config import get_config
@app.get("/infor")
def get_infor():
    settings = get_config()
    return {
        "app_name": settings.app_name,
        "author": settings.author,
        "app_mode": settings.app_mode,
        "port": settings.port,
        "reload": settings.reload,
    }

from services.ollama_client import get_ollama_client
from pydantic import BaseModel

class OllamaRequest(BaseModel):
    prompt: str

@app.post("/ollama")
def ollama_chat(request: OllamaRequest):
    client = get_ollama_client()
    return client.chat(request.prompt)