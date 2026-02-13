from collections import Counter
from typing import Annotated

from fastapi import Depends, HTTPException
from httpx import Response
from pydantic import HttpUrl

from app.api.v1.codeberg.models.foreign.repository import Repositories
from app.api.v1.shared.service import BaseService


class CodebergService(BaseService):
    async def get_user_languages(self, username: str) -> dict[str, int]:
        repositories: Repositories = await self.__fetch_user_repos(username)
        languages: Counter[str] = Counter()

        for repo in repositories.repositories:
            repo_languages: dict[str, int] = await self.__fetch_repo_languages(repo.languages_url)
            languages += repo_languages

        return dict[str, int](languages)

    async def __fetch_repo_languages(self, languages_url: HttpUrl) -> dict[str, int]:
        url: str = languages_url.encoded_string()

        resp: Response = await self._client.get(url)
        if resp.status_code != 200:
            raise HTTPException(resp.status_code, detail=resp.json())

        languages = resp.json()
        return languages

    async def __fetch_user_repos(self, username: str) -> Repositories:
        url: str = f"https://codeberg.org/api/v1/users/{username}/repos"

        resp: Response = await self._client.get(url)
        if resp.status_code != 200:
            raise HTTPException(resp.status_code, detail=resp.json())

        repositories = resp.json()
        return Repositories.model_validate({"repositories": repositories})


type CodebergServiceDependency = Annotated[CodebergService, Depends()]
