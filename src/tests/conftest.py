import pytest

from app.api.v1.codeberg.models.repository import Repository as CodebergRepository
from app.api.v1.github.models.repository import Repository as GitHubRepository
from tests.factories.codeberg_factory import CodebergRepositoryFactory
from tests.factories.github_factory import GitHubRepositoryFactory


@pytest.fixture
async def test_codeberg_repository() -> CodebergRepository:
    repo: CodebergRepository = await CodebergRepositoryFactory.create_async()
    return repo


@pytest.fixture
async def test_github_repository() -> GitHubRepository:
    repo: GitHubRepository = await GitHubRepositoryFactory.create_async()
    return repo
