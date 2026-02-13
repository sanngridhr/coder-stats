import asyncio
from collections import Counter
from typing import Annotated

from fastapi import Depends
from httpx import Response
from pydantic import HttpUrl

from app.api.core.query_params.models import LanguagesQueryParams
from app.api.core.service import BaseService
from app.api.v1.codeberg.models.foreign import Repositories


class CodebergService(BaseService):
    async def get_user_languages(self, username: str, params: LanguagesQueryParams) -> dict[str, int]:
        repositories: Repositories = await self.__fetch_user_repos(username)
        languages: Counter[str] = Counter()

        languages_list: list[dict[str, int]] = await asyncio.gather(
            *[self.__fetch_repo_languages(repo.languages_url) for repo in repositories.repositories]
        )
        for languages_item in languages_list:
            languages += languages_item

        return params.sort_languages(languages)

    async def __fetch_repo_languages(self, languages_url: HttpUrl) -> dict[str, int]:
        url: str = languages_url.encoded_string()

        resp: Response = await self._get(url)
        languages = resp.json()

        return languages

    async def __fetch_user_repos(self, username: str) -> Repositories:
        url: str = f"https://codeberg.org/api/v1/users/{username}/repos"

        resp: Response = await self._get(url)
        repositories = resp.json()

        return Repositories.model_validate({"repositories": repositories})


type CodebergServiceDependency = Annotated[CodebergService, Depends()]
