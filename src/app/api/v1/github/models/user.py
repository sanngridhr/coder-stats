from pydantic import BaseModel, HttpUrl

from app.api.v1.github.constants.enums import UserType


class User(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: HttpUrl
    gravatar_id: str
    url: HttpUrl
    html_url: HttpUrl
    followers_url: HttpUrl
    following_url: HttpUrl
    gists_url: HttpUrl
    starred_url: HttpUrl
    subscriptions_url: HttpUrl
    organizations_url: HttpUrl
    repos_url: HttpUrl
    events_url: HttpUrl
    received_events_url: HttpUrl
    type: UserType
    site_admin: bool
