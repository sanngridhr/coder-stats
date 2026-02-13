from fastapi.routing import APIRouter

from app.api.core.query_params.models import LanguagesQueryParamsDependency
from app.api.v1.codeberg.models.responses import DetailWith, MessageAndUrl
from app.api.v1.codeberg.service import CodebergServiceDependency

router: APIRouter = APIRouter(
    prefix="/codeberg",
    responses={404: {"model": DetailWith[MessageAndUrl]}},
)


@router.get("/{username}/languages")
async def get_user_languages(
    service: CodebergServiceDependency,
    params: LanguagesQueryParamsDependency,
    username: str,
) -> dict[str, int]:
    return await service.get_user_languages(username, params)
