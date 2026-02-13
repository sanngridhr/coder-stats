from datetime import datetime

from pydantic import BaseModel, HttpUrl

from app.api.v1.codeberg.constants.enums import ExternalTrackerStyle, MergeStyle, ObjectFormatName, UpdateStyle
from app.api.v1.shared.types import EmptyStr, SshUrl

from .team import Team
from .user import User


class ExternalTracker(BaseModel):
    external_tracker_format: str
    external_tracker_regexp_pattern: str
    external_tracker_style: ExternalTrackerStyle
    external_tracker_url: HttpUrl


class ExternalWiki(BaseModel):
    external_wiki_url: HttpUrl


class InternalTracker(BaseModel):
    allow_only_contributors_to_track_time: bool
    enable_issue_dependencies: bool
    enable_time_tracker: bool


class Permissions(BaseModel):
    admin: bool
    pull: bool
    push: bool


class RepoTransfer(BaseModel):
    doer: User
    recipient: User
    teams: list[Team]


class Repository(BaseModel):
    allow_fast_forward_only_merge: bool
    allow_merge_commits: bool
    allow_rebase: bool
    allow_rebase_explicit: bool
    allow_rebase_update: bool
    allow_squash_merge: bool
    archived: bool
    archived_at: datetime
    avatar_url: HttpUrl | EmptyStr
    clone_url: HttpUrl
    created_at: datetime
    default_allow_maintainer_edit: bool
    default_branch: str
    default_delete_branch_after_merge: bool
    default_merge_style: MergeStyle
    default_update_style: UpdateStyle
    description: str
    empty: bool
    external_tracker: ExternalTracker | None = None
    external_wiki: ExternalWiki | None = None
    fork: bool
    forks_count: int
    full_name: str
    globally_editable_wiki: bool
    has_actions: bool
    has_issues: bool
    has_packages: bool
    has_projects: bool
    has_pull_requests: bool
    has_wiki: bool
    html_url: HttpUrl
    id: int
    ignore_whitespace_conflicts: bool
    internal: bool
    internal_tracker: InternalTracker
    language: str
    languages_url: HttpUrl
    link: HttpUrl | EmptyStr
    mirror: bool
    mirror_interval: str
    mirror_updated: datetime
    name: str
    object_format_name: ObjectFormatName
    owner: User
    parent: Repository | None
    permissions: Permissions
    private: bool
    release_counter: int
    repo_transfer: RepoTransfer | None
    size: int
    ssh_url: SshUrl
    stars_count: int
    template: bool
    topics: list[str]
    updated_at: datetime
    url: HttpUrl
    watchers_count: int
    website: HttpUrl | EmptyStr
    wiki_branch: str


class Repositories(BaseModel):
    repositories: list[Repository]
