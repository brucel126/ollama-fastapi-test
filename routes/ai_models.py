from fastapi import APIRouter
import httpx
from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_PORT = os.getenv("OLLAMA_PORT")

ai_models_router = APIRouter()

@ai_models_router.get("/api/models")
async def get_ai_models():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{OLLAMA_BASE_URL}:{OLLAMA_PORT}/api/tags")
        return {"data": response.json()}