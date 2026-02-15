import asyncio
from collections import Counter
from typing import Annotated, Any

from fastapi import Depends

from app.api.core.query_params.models import TextQueryParams
from app.api.core.services.base_service import BaseService
from app.api.v1.codeberg.models.foreign import Repositories


class CodebergService(BaseService):
    async def get_user_languages(self, username: str, params: TextQueryParams | None = None) -> dict[str, int]:  # pyright: ignore[reportRedeclaration]
        repositories: Repositories = await self.__fetch_user_repos(username)
        languages: Counter[str] = Counter()

        languages_list: list[dict[str, int]] = await asyncio.gather(
            *[self.__fetch_repo_languages(str(repo.languages_url)) for repo in repositories.repositories]
        )
        for languages_item in languages_list:
            languages += languages_item

        if params is None:
            params: TextQueryParams = TextQueryParams()

        return params.sort_languages(languages)

    async def __fetch_repo_languages(self, languages_url: str) -> dict[str, int]:
        languages: dict[str, int] = await self._get(languages_url)
        return languages

    async def __fetch_user_repos(self, username: str) -> Repositories:
        url: str = f"https://codeberg.org/api/v1/users/{username}/repos"

        repositories: list[dict[str, Any]] = await self._get(url)
        return Repositories.model_validate({"repositories": repositories})


type CodebergServiceDependency = Annotated[CodebergService, Depends()]
