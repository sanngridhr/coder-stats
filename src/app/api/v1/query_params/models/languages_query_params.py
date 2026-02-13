from typing import Annotated

from fastapi import Depends

from app.api.v1.query_params.models.mixins import LimitMixin, SortOrderMixin


class LanguagesQueryParams(LimitMixin, SortOrderMixin):
    def sort_languages(self, languages: dict[str, int]) -> dict[str, int]:
        languages_items: list[tuple[str, int]] = (
            list(languages.items()) if self.limit is None else list(languages.items())[self.limit :]
        )

        return dict(sorted(languages_items, key=lambda item: item[1], reverse=(self.sort_order == "desc")))


type LanguagesQueryParamsDependency = Annotated[LanguagesQueryParams, Depends()]
