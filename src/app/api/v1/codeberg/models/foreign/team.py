from pydantic import BaseModel, EmailStr, Field, HttpUrl

from app.api.v1.codeberg.constants.enums import Permission, Unit, Visibility


class Organization(BaseModel):
    avatar_url: HttpUrl
    description: str
    email: EmailStr
    full_name: str
    id: int
    location: str
    name: str
    repo_admin_change_team_access: bool
    username: str = Field(deprecated=True)
    visibility: Visibility
    website: HttpUrl


class Team(BaseModel):
    can_create_org_repo: bool
    description: str
    id: int
    includes_all_repositories: bool
    name: str
    organization: Organization
    permission: Permission
    units: set[Unit]
    units_map: dict[Unit, Permission]
