from pydantic import BaseModel

from app.api.core.query_params.constants.enums import SortOrder


class SortOrderMixin(BaseModel):
    sort_order: SortOrder = SortOrder.DESCENDING
