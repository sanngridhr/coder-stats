from pydantic import BaseModel


class MessageAndUrl(BaseModel):
    message: str
    url: str


class DetailWith[T](BaseModel):
    detail: T
