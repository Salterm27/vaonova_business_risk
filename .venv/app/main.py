from fastapi import FastAPI
from app.routes import labour

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(labour.router)