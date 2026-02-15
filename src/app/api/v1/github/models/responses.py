from pydantic import BaseModel


class MessageAndUrl(BaseModel):
    message: str
    documentation_url: str
