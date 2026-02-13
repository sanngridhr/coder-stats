from pydantic import BaseModel

from app.api.v1.query_params.constants.enums import SortOrder


class SortOrderMixin(BaseModel):
    sort_order: SortOrder
