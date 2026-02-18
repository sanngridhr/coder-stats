from polyfactory.factories.pydantic_factory import ModelFactory

from app.api.v1.github.models.repository import Repository


class GitHubRepositoryFactory(ModelFactory[Repository]):
    __model__ = Repository
