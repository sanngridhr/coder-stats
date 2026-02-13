from pydantic import BaseModel, PositiveInt


class LimitMixin(BaseModel):
    limit: PositiveInt | None = None
