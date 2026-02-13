from typing import Annotated

from fastapi import Depends

from app.api.core.query_params.models.mixins import LimitMixin, SortOrderMixin


class LanguagesQueryParams(LimitMixin, SortOrderMixin):
    def sort_languages(self, languages: dict[str, int]) -> dict[str, int]:
        sorted_languages: dict[str, int] = dict(
            sorted(
                languages.items(),
                key=lambda item: item[1],
                reverse=(self.sort_order == "desc"),
            )
        )
        if self.limit is None:
            return sorted_languages
        else:
            return dict(list(sorted_languages.items())[: self.limit])


type LanguagesQueryParamsDependency = Annotated[LanguagesQueryParams, Depends()]
