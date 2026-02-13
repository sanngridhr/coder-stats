from httpx import AsyncClient

from app.api.v1.shared.client import AsyncClientDependency


class BaseService:
    _client: AsyncClient

    def __init__(self, client: AsyncClientDependency) -> None:
        self._client = client
