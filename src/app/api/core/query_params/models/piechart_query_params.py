from typing import Annotated

from fastapi import Depends
from pydantic import Field, PositiveFloat, model_validator

from app.api.core.query_params.constants.enums import Direction, Theme
from app.api.core.query_params.models import BaseQueryParams


class PieChartQueryParams(BaseQueryParams):
    direction: Direction = Direction.CLOCKWISE
    font: str = "sans"
    gap: PositiveFloat = 0.05
    lump_small_data: bool = True
    radius: PositiveFloat = 0.8
    start_angle: float = Field(default=90, ge=0, lt=360)
    theme: Theme = Theme.FLEXOKI_DARK
    theme_reverse: bool = False
    theme_transparency: str = Field(default="FF", pattern=r"[0-9A-F]{2}")
    width: PositiveFloat = 0.2

    @model_validator(mode="before")
    @classmethod
    def auto_limit(cls, data: dict) -> dict:
        if data["limit"] == "auto":
            theme: Theme = data["theme"]
            data["limit"] = len(theme.get_colours())
        return data


type PieChartQueryParamsDependency = Annotated[PieChartQueryParams, Depends()]
