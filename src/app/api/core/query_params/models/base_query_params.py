from typing import Literal

from pydantic import BaseModel, ConfigDict, PositiveInt


class BaseQueryParams(BaseModel):
    model_config: ConfigDict = ConfigDict(frozen=True)

    limit: PositiveInt | Literal["auto"] = "auto"
    include_forked: bool = False
