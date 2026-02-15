import asyncio
from collections import Counter
from typing import Annotated, Any

from fastapi import Depends

from app.api.core.services.base_service import BaseService
from app.api.v1.github.models.repository import Repositories


class GitHubService(BaseService):
    async def get_user_languages(self, username: str, include_forked: bool) -> dict[str, int]:
        repositories: Repositories = await self.__fetch_user_repos(username)
        languages: Counter[str] = Counter()

        languages_list: list[dict[str, int]] = await asyncio.gather(
            *[
                self.__fetch_repo_languages(str(repo.languages_url))
                for repo in repositories.repositories
                if repo.fork == include_forked
            ]
        )
        for languages_item in languages_list:
            languages += languages_item

        return languages

    async def __fetch_repo_languages(self, languages_url: str) -> dict[str, int]:
        languages: dict[str, int] = await self._get(languages_url)
        return languages

    async def __fetch_user_repos(self, username: str) -> Repositories:
        url: str = f"https://api.github.com/users/{username}/repos"

        repositories: list[dict[str, Any]] = await self._get(url)
        return Repositories.model_validate({"repositories": repositories})


type GitHubServiceDependency = Annotated[GitHubService, Depends()]
