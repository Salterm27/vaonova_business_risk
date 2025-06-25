from fastapi import FastAPI
from app.routes import labour_routes

from dotenv import load_dotenv
import os

load_dotenv()  # 👈 loads from .env

OPENAI_API_KEY = os.getenv("openai_key")
MONGO_URI = os.getenv("MONGO_URI")


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(labour_routes.router)