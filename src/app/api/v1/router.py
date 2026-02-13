from fastapi.routing import APIRouter

from app.api.v1.codeberg.routes import router as codeberg_router

router: APIRouter = APIRouter(prefix="/v1")
router.include_router(codeberg_router)
