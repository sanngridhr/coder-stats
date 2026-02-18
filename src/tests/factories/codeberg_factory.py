from polyfactory.factories.pydantic_factory import ModelFactory

from app.api.v1.codeberg.models.repository import Repository


class CodebergRepositoryFactory(ModelFactory[Repository]):
    __model__ = Repository
