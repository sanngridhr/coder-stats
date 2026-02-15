from pydantic import BaseModel


class DetailWith[T](BaseModel):
    detail: T
