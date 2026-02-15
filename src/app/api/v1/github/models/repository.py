from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl

from app.api.core.types import EmptyStr, GitUrl
from app.api.v1.github.constants.enums import Visibility
from app.api.v1.github.models.user import User


class Permissions(BaseModel):
    admin: bool
    push: bool
    pull: bool


class Repository(BaseModel):
    archive_url: HttpUrl
    archived: bool
    assignees_url: HttpUrl
    blobs_url: HttpUrl
    branches_url: HttpUrl
    clone_url: HttpUrl
    collaborators_url: HttpUrl
    comments_url: HttpUrl
    commits_url: HttpUrl
    compare_url: HttpUrl
    contents_url: HttpUrl
    contributors_url: HttpUrl
    created_at: datetime
    default_branch: str
    deployments_url: HttpUrl
    description: str | None
    disabled: bool
    downloads_url: HttpUrl
    events_url: HttpUrl
    fork: bool
    forks_count: int
    forks_url: HttpUrl
    full_name: str
    git_commits_url: HttpUrl
    git_refs_url: HttpUrl
    git_tags_url: HttpUrl
    git_url: GitUrl
    has_discussions: bool
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: HttpUrl | EmptyStr | None
    hooks_url: HttpUrl
    html_url: HttpUrl
    id: int
    is_template: bool
    issue_comment_url: HttpUrl
    issue_events_url: HttpUrl
    keys_url: HttpUrl
    labels_url: HttpUrl
    language: str | None
    languages_url: HttpUrl
    merges_url: HttpUrl
    milestones_url: HttpUrl
    mirror_url: HttpUrl | None
    name: str
    node_id: str
    notifications_url: HttpUrl
    open_issues_count: int
    owner: User
    permissions: Permissions | None = None
    private: bool
    pulls_url: HttpUrl
    pushed_at: datetime
    releases_url: HttpUrl
    security_and_analysis: dict[str, dict[str, Literal["enabled", "disabled"]]] | None = None
    size: int
    ssh_url: str = Field(pattern=r"git@github\.com:.+?\/.+?\.git")
    stargazers_count: int
    stargazers_url: HttpUrl
    statuses_url: HttpUrl
    subscribers_url: HttpUrl
    svn_url: HttpUrl
    tags_url: HttpUrl
    teams_url: HttpUrl
    topics: list[str]
    trees_url: HttpUrl
    updated_at: datetime
    url: HttpUrl
    visibility: Visibility
    watchers_count: int


class Repositories(BaseModel):
    repositories: list[Repository]
