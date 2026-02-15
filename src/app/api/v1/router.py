from fastapi.routing import APIRouter

from app.api.v1.codeberg.routes import router as codeberg_router
from app.api.v1.github.routes import router as github_router

router: APIRouter = APIRouter(prefix="/v1")
router.include_router(router=codeberg_router)
router.include_router(router=github_router)
