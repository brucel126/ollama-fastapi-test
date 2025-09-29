from fastapi import APIRouter
import httpx

ai_models_router = APIRouter()

@ai_models_router.get("/api/models")
async def get_ai_models():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:11434/api/tags")
        return {"data": response.json()}