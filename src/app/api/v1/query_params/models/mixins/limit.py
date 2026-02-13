from pydantic import BaseModel, Field, NonNegativeInt


class LimitMixin(BaseModel):
    limit: NonNegativeInt | None = None
