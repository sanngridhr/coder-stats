import asyncio
from abc import ABC, abstractmethod
from typing import Any, Counter

from aiocache import cached
from fastapi import HTTPException
from httpx import URL, AsyncClient, Response

from app.api.core.client import AsyncClientDependency
from app.api.core.models.model_list import ModelList


class GitService(ABC):
    _client: AsyncClient

    def __init__(self, client: AsyncClientDependency) -> None:
        self._client = client

    async def get_user_languages(self, username: str, include_forked: bool) -> dict[str, int]:
        repositories: ModelList[Any] = await self._fetch_user_repos(username)
        languages: Counter[str] = Counter()

        languages_list: list[dict[str, int]] = await asyncio.gather(
            *[
                self._fetch_repo_languages(str(repo.languages_url))
                for repo in repositories.models
                if include_forked or not repo.fork
            ]
        )
        for languages_item in languages_list:
            languages += languages_item

        return languages

    async def _fetch_repo_languages(self, languages_url: str) -> dict[str, int]:
        languages: dict[str, int] = await self._get(languages_url)
        return languages

    @abstractmethod
    async def _fetch_user_repos(self, username: str) -> ModelList: ...

    @cached(ttl=300, noself=True)
    async def _get(self, url: str | URL, **kwargs) -> Any:
        resp: Response = await self._client.get(url, **kwargs)
        if resp.status_code != 200:
            raise HTTPException(resp.status_code, detail=resp.json())

        return resp.json()
