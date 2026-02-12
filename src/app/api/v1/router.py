from fastapi.routing import APIRouter

from app.api.v1.github.routes import router as github_router

router: APIRouter = APIRouter(prefix="/v1")
router.include_router(github_router)
