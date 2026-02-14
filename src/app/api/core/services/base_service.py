from typing import Any

from aiocache import cached
from fastapi import HTTPException
from httpx import URL, AsyncClient, Response

from app.api.core.client import AsyncClientDependency


class BaseService:
    _client: AsyncClient

    def __init__(self, client: AsyncClientDependency) -> None:
        self._client = client

    @cached(ttl=300, noself=True)
    async def _get(self, url: str | URL) -> Any:
        resp: Response = await self._client.get(url)
        if resp.status_code != 200:
            raise HTTPException(resp.status_code, detail=resp.json())

        return resp.json()
