from fastapi.routing import APIRouter

from app.api.v1.codeberg.service import CodebergServiceDependency

router: APIRouter = APIRouter(prefix="/codeberg")


@router.get("/{username}/languages_total")
async def get_user_languages(
    service: CodebergServiceDependency,
    username: str,
) -> dict[str, int]:
    return await service.get_user_languages(username)
