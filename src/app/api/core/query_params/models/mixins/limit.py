from pydantic import BaseModel, PositiveInt


class LimitMixin(BaseModel):
    model_config = {"frozen": True}

    limit: PositiveInt | None = None
