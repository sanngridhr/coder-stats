from typing import Literal

from fastapi.routing import APIRouter

from app.api.v1.router import router as v1_router

router: APIRouter = APIRouter(prefix="/api")
router.include_router(v1_router)


@router.get("/health", tags=["health"])
async def health() -> Literal["OK"]:
    return "OK"
