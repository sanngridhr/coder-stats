from datetime import datetime

from pydantic import BaseModel, EmailStr, HttpUrl

from app.api.v1.codeberg.constants.enums import Visibility


class User(BaseModel):
    active: bool
    avatar_url: HttpUrl
    created: datetime
    description: str
    email: EmailStr
    followers_count: int
    full_name: str
    html_url: HttpUrl
    id: int
    is_admin: bool
    language: str
    last_login: datetime
    location: str
    login: str
    login_name: str
    prohibit_login: bool
    pronouns: str
    restricted: bool
    source_id: int
    starred_repos_count: int
    visibility: Visibility
    website: HttpUrl
