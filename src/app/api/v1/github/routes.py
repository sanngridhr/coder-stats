from fastapi.routing import APIRouter

router: APIRouter = APIRouter(prefix="/github")


@router.get("/{user}/languages_total")
async def get_user_languages(): ...
