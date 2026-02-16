from abc import ABC, abstractmethod
import asyncio
from typing import Any, Counter

from aiocache import cached
from fastapi import HTTPException
from httpx import URL, AsyncClient, Response

from app.api.core.client import AsyncClientDependency
from app.api.core.models.list_model import ModelList


class BaseService(ABC):
    _client: AsyncClient

    def __init__(self, client: AsyncClientDependency) -> None:
        self._client = client
    
    async def get_user_languages(self, username: str, include_forked: bool) -> dict[str, int]:
        repositories: ModelList[Any] = await self._fetch_user_repos(username)
        languages: Counter[str] = Counter()

        languages_list: list[dict[str, int]] = await asyncio.gather(
            *[
                self._fetch_repo_languages(str(repo.languages_url))
                for repo in repositories.model
                if repo.fork == include_forked
            ]
        )
        for languages_item in languages_list:
            languages += languages_item

        return languages

    @abstractmethod
    async def _fetch_repo_languages(self, languages_url: str) -> dict[str, int]: ...

    @abstractmethod
    async def _fetch_user_repos(self, username: str) -> ModelList: ...


    @cached(ttl=300, noself=True)
    async def _get(self, url: str | URL) -> Any:
        resp: Response = await self._client.get(url)
        if resp.status_code != 200:
            raise HTTPException(resp.status_code, detail=resp.json())

        return resp.json()
