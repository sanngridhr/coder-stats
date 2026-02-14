from fastapi import Response
from fastapi.routing import APIRouter
from matplotlib.figure import Figure

from app.api.core.query_params.models import LanguagesQueryParamsDependency
from app.api.core.services.datavis_service import DataVisServiceDependency
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


@router.get("/{username}/languages/pie.svg")
async def get_user_languages_pie(
    service: CodebergServiceDependency,
    datavis_service: DataVisServiceDependency,
    params: LanguagesQueryParamsDependency,
    username: str,
) -> Response:
    languages: dict[str, int] = await service.get_user_languages(username, params)

    fig: Figure = await datavis_service.get_donut_chart(languages)

    return await datavis_service.to_svg(fig)
