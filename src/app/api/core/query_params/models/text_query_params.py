from typing import Annotated

from fastapi import Depends

from app.api.core.query_params.enums import SortOrder
from app.api.core.query_params.models.base_query_params import BaseQueryParams


class TextQueryParams(BaseQueryParams):
    sort_order: SortOrder = SortOrder.DESCENDING

    def sort(self, data: dict[str, int]) -> dict[str, int]:
        sorted_data: dict[str, int] = dict(
            sorted(
                data.items(),
                key=lambda item: item[1],
                reverse=(self.sort_order == "desc"),
            )
        )
        if self.limit == "auto":
            return sorted_data
        else:
            return dict(list(sorted_data.items())[: self.limit])


type TextQueryParamsDependency = Annotated[TextQueryParams, Depends()]
