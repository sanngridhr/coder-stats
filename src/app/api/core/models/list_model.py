from pydantic import BaseModel


class ModelList[T](BaseModel):
    model: list[T]
