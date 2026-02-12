from typing import Annotated, TypeAlias

from fastapi import Depends


class CodebergService: ...


def _get_codeberg_service() -> CodebergService:
    return CodebergService()


CodebergServiceDependency: TypeAlias = Annotated[CodebergService, Depends(dependency=_get_codeberg_service)]
