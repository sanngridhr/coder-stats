from fastapi import APIRouter, Response
from matplotlib.figure import Figure

from app.api.core.models.responses import DetailWith
from app.api.core.query_params.models import (
    PieChartQueryParamsDependency,
    TextQueryParamsDependency,
)
from app.api.core.services.datavis_service import DataVisServiceDependency
from app.api.v1.github.models.responses import MessageAndUrl
from app.api.v1.github.service import GitHubServiceDependency

router: APIRouter = APIRouter(
    prefix="/github",
    tags=["github"],
    responses={404: {"model": DetailWith[MessageAndUrl]}},
)


@router.get("/{username}/languages")
async def get_user_languages(
    service: GitHubServiceDependency,
    params: TextQueryParamsDependency,
    username: str,
) -> dict[str, int]:
    languages: dict[str, int] = await service.get_user_languages(username, params.include_forked)

    return params.sort(languages)


@router.get("/{username}/languages/pie.svg")
async def get_user_languages_pie(
    service: GitHubServiceDependency,
    datavis_service: DataVisServiceDependency,
    params: PieChartQueryParamsDependency,
    username: str,
) -> Response:
    languages: dict[str, int] = await service.get_user_languages(username, params.include_forked)
    data: dict[str, int] = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))

    fig: Figure = datavis_service.get_donut_chart(data, params)
    return datavis_service.to_svg(fig)
