from pydantic import BaseModel


class ModelList[T](BaseModel):
    models: list[T]
