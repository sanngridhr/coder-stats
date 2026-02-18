from fastapi import Response
from fastapi.routing import APIRouter
from matplotlib.figure import Figure

from app.api.core.constants.enums import Tags
from app.api.core.query_params.models import (
    PieChartQueryParamsDependency,
    TextQueryParamsDependency,
)
from app.api.core.services.datavis_service import DataVisServiceDependency
from app.api.core.services.factories.get_service import GitServiceDependency

router: APIRouter = APIRouter(prefix="/v1")


@router.get("/{provider}/u/{username}/languages", tags=[Tags.USER])
async def get_user_languages(
    service: GitServiceDependency,
    params: TextQueryParamsDependency,
    username: str,
) -> dict[str, int]:
    languages: dict[str, int] = await service.get_user_languages(username, params.include_forks)
    return params.sort(languages)


@router.get("/{provider}/u/{username}/languages/pie.svg", tags=[Tags.USER])
async def get_user_languages_pie(
    service: GitServiceDependency,
    datavis_service: DataVisServiceDependency,
    params: PieChartQueryParamsDependency,
    username: str,
) -> Response:
    languages: dict[str, int] = await service.get_user_languages(username, params.include_forks)
    data: dict[str, int] = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))
    fig: Figure = datavis_service.get_donut_chart(data, params)
    svg: bytes = datavis_service.to_svg(fig)
    return Response(content=svg, media_type="image/svg+xml")
