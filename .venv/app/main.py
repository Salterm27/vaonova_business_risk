from fastapi import FastAPI
from app.routes import labour

from dotenv import load_dotenv
import os

load_dotenv()  # 👈 loads from .env

OPENAI_API_KEY = os.getenv("openai_key")


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(labour.router)