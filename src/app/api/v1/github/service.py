from typing import Annotated, Any

from fastapi import Depends

from app.api.core.models.list_model import ModelList
from app.api.core.services.base_service import BaseService
from app.api.v1.github.models.repository import Repository


class GitHubService(BaseService):
    async def _fetch_repo_languages(self, languages_url: str) -> dict[str, int]:
        languages: dict[str, int] = await self._get(languages_url)
        return languages

    async def _fetch_user_repos(self, username: str) -> ModelList:
        url: str = f"https://api.github.com/users/{username}/repos"

        repositories: list[dict[str, Any]] = await self._get(url)
        return ModelList[Repository].model_validate({"repositories": repositories})


type GitHubServiceDependency = Annotated[GitHubService, Depends()]
