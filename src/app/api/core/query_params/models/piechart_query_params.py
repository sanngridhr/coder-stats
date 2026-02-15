from typing import Annotated

from fastapi import Depends
from pydantic import Field, PositiveFloat, PositiveInt

from app.api.core.query_params.constants.enums import Direction, Theme
from app.api.core.query_params.models import BaseQueryParams


class PieChartQueryParams(BaseQueryParams):
    direction: Direction = Direction.CLOCKWISE
    font: str = "sans"
    gap: PositiveFloat = 0.05
    limit: PositiveInt | None = None
    lump_small_data: bool = True
    radius: PositiveFloat = 1.0
    start_angle: float = Field(default=90, ge=0, lt=360)
    theme: Theme = Theme.FLEXOKI_DARK
    width: PositiveFloat = 0.2
    theme_reverse: bool = False
    theme_transparency: str = Field(default="FF", pattern=r"[0-9A-F]{2}")


type PieChartQueryParamsDependency = Annotated[PieChartQueryParams, Depends()]
