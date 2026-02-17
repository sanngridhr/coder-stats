from enum import StrEnum


class UserType(StrEnum):
    USER = "User"
    ORGANIZATION = "Organization"


class Visibility(StrEnum):
    PUBLIC = "public"
