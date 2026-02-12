from typing import Literal

from api.v1.router import router as v1_router
from fastapi.routing import APIRouter

router: APIRouter = APIRouter(prefix="/api")
router.include_router(v1_router)


@router.get("/health")
async def health() -> Literal["OK"]:
    return "OK"
