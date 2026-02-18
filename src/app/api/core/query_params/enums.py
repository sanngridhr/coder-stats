from enum import StrEnum


class Direction(StrEnum):
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anti-clockwise"


class SortOrder(StrEnum):
    ASCENDING = "asc"
    DESCENDING = "desc"
