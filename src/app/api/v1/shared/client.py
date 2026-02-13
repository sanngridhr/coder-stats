from typing import Annotated, AsyncGenerator

from fastapi import Depends
from httpx import AsyncClient


async def _get_async_client() -> AsyncGenerator[AsyncClient]:
    client: AsyncClient = AsyncClient()
    try:
        yield client
    finally:
        await client.aclose()


type AsyncClientDependency = Annotated[AsyncClient, Depends(_get_async_client)]
