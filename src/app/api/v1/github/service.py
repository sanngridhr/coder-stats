from typing import Annotated, TypeAlias

from fastapi import Depends


class GitHubService: ...


def _get_github_service() -> GitHubService:
    return GitHubService()


GitHubServiceDependency: TypeAlias = Annotated[GitHubService, Depends(dependency=_get_github_service)]
