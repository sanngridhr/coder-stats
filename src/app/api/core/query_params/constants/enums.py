from enum import StrEnum


class SortOrder(StrEnum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class Direction(StrEnum):
    CLOCKWISE = "clockwise"
    ANTICLOCKWISE = "anti-clockwise"


class Theme(StrEnum):
    FLEXOKI_DARK = "flexoki-dark"
    FLEXOKI_LIGHT = "flexoki-light"
