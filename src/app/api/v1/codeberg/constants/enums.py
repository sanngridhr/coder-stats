from enum import StrEnum


class ExternalTrackerStyle(StrEnum):
    ALPHANUMERIC = "alphanumeric"
    NUMERIC = "numeric"
    REGEXP = "regexp"


class MergeStyle(StrEnum):
    MERGE = "merge"


class ObjectFormatName(StrEnum):
    SHA1 = "sha1"
    SHA256 = "sha256"


class Permission(StrEnum):
    NONE = "none"
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"
    OWNER = "owner"


class Unit(StrEnum):
    CODE = "repo.code"
    EXT_ISSUES = "repo.ext_issues"
    EXT_WIKI = "repo.ext_wiki"
    ISSUES = "repo.issues"
    PROJECTS = "repo.projects"
    PULLS = "repo.pulls"
    RELEASES = "repo.releases"
    WIKI = "repo.wiki"


class UpdateStyle(StrEnum):
    MERGE = "merge"


class Visibility(StrEnum):
    LIMITED = "limited"
    PRIVATE = "private"
    PUBLIC = "public"
