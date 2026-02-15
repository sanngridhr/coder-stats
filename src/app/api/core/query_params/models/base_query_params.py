from pydantic import BaseModel, ConfigDict


class BaseQueryParams(BaseModel):
    model_config: ConfigDict = ConfigDict(frozen=True)
