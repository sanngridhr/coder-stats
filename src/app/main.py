from typing import Literal

from fastapi import FastAPI

from app.api.router import router

app: FastAPI = FastAPI()
app.include_router(router)


@app.get("/health", tags=["health"])
async def health() -> Literal["OK"]:
    return "OK"
