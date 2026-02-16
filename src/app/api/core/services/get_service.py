from typing import Annotated

from fastapi import Depends, Path

from app.api.core.services.git_service import GitService
from app.api.core.services.constants.enums import GitProvider
from app.api.v1.codeberg.service import CodebergService
from app.api.v1.github.service import GitHubService


def __get_service(
    provider: Annotated[GitProvider, Path()],
    codeberg_service: Annotated[CodebergService, Depends()],
    github_service: Annotated[GitHubService, Depends()],
) -> GitService:
    match provider:
        case GitProvider.CODEBERG:
            return codeberg_service
        case GitProvider.GITHUB:
            return github_service

GitServiceDependency = Annotated[GitService, Depends(__get_service)]