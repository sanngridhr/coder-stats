from enum import StrEnum


class SortOrder(StrEnum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class Direction(StrEnum):
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anti-clockwise"
