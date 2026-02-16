from typing import Any

from app.api.core.models.model_list import ModelList
from app.api.core.services.git_service import GitService
from app.api.v1.codeberg.models.repository import Repository


class CodebergService(GitService):
    async def _fetch_user_repos(self, username: str) -> ModelList:
        url: str = f"https://codeberg.org/api/v1/users/{username}/repos"

        repositories: list[dict[str, Any]] = await self._get(url)
        return ModelList[Repository].model_validate({"models": repositories})
