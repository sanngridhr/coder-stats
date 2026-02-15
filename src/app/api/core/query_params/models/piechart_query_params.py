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

    def get_colours(self) -> list[str]:
        match self.theme:
            case Theme.FLEXOKI_DARK:
                return [
                    "#D14D41",  # red
                    "#DA702C",  # orange
                    "#D0A215",  # yellow
                    "#879A39",  # green
                    "#3AA99F",  # cyan
                    "#4385BE",  # blue
                    "#8B7EC8",  # purple
                    "#CE5D97",  # magenta
                ]
            case Theme.FLEXOKI_LIGHT:
                return [
                    "#AF3029",  # red
                    "#BC5215",  # orange
                    "#AD8301",  # yellow
                    "#66800B",  # green
                    "#24837B",  # cyan
                    "#205EA6",  # blue
                    "#5E409D",  # purple
                    "#A02F6F",  # magenta
                ]


type PieChartQueryParamsDependency = Annotated[PieChartQueryParams, Depends()]
