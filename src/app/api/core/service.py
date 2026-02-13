from fastapi import HTTPException
from httpx import URL, AsyncClient, Response

from app.api.core.client import AsyncClientDependency


class BaseService:
    _client: AsyncClient

    def __init__(self, client: AsyncClientDependency) -> None:
        self._client = client

    async def _get(self, url: str | URL) -> Response:
        resp: Response = await self._client.get(url)
        if resp.status_code != 200:
            raise HTTPException(resp.status_code, detail=resp.json())

        return resp
