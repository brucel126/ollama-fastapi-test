from fastapi import FastAPI
from routes import ai_models_router

app = FastAPI()

app.include_router(ai_models_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}