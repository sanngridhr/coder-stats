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
    FLEXOKI_BASE = "flexoki-base"
    FLEXOKI_RED = "flexoki-red"
    FLEXOKI_ORANGE = "flexoki-orange"
    FLEXOKI_YELLOW = "flexoki-yellow"
    FLEXOKI_GREEN = "flexoki-green"
    FLEXOKI_CYAN = "flexoki-cyan"
    FLEXOKI_BLUE = "flexoki-blue"
    FLEXOKI_PURPLE = "flexoki-purple"
    FLEXOKI_MAGENTA = "flexoki-magenta"

    def get_colours(self) -> list[str]:
        match self:
            case Theme.FLEXOKI_DARK:
                return [
                    "#D14D41",  # re
                    "#DA702C",  # or
                    "#D0A215",  # ye
                    "#879A39",  # gr
                    "#3AA99F",  # cy
                    "#4385BE",  # bl
                    "#8B7EC8",  # pu
                    "#CE5D97",  # ma
                ]
            case Theme.FLEXOKI_LIGHT:
                return [
                    "#AF3029",  # re
                    "#BC5215",  # or
                    "#AD8301",  # ye
                    "#66800B",  # gr
                    "#24837B",  # cy
                    "#205EA6",  # bl
                    "#5E409D",  # pu
                    "#A02F6F",  # ma
                ]
            case Theme.FLEXOKI_BASE:
                return [
                    "#F2F0E5",  # 50
                    "#E6E4D9",  # 100
                    "#DAD8CE",  # 150
                    "#CECDC3",  # 200
                    "#B7B5AC",  # 300
                    "#9F9D96",  # 400
                    "#878580",  # 500
                    "#6F6E69",  # 600
                    "#575653",  # 700
                    "#403E3C",  # 800
                    "#343331",  # 850
                    "#282726",  # 900
                    "#1C1B1A",  # 950
                ]
            case Theme.FLEXOKI_RED:
                return [
                    "#FFE1D5",  # 50
                    "#FFCABB",  # 100
                    "#FDB2A2",  # 150
                    "#F89A8A",  # 200
                    "#E8705F",  # 300
                    "#D14D41",  # 400
                    "#C03E35",  # 500
                    "#AF3029",  # 600
                    "#942822",  # 700
                    "#6C201C",  # 800
                    "#551B18",  # 850
                    "#3E1715",  # 900
                    "#261312",  # 950
                ]
            case Theme.FLEXOKI_ORANGE:
                return [
                    "#FFE7CE",  # 50
                    "#FED3AF",  # 100
                    "#FCC192",  # 150
                    "#F9AE77",  # 200
                    "#EC8B49",  # 300
                    "#DA702C",  # 400
                    "#CB6120",  # 500
                    "#BC5215",  # 600
                    "#9D4310",  # 700
                    "#71320D",  # 800
                    "#59290D",  # 850
                    "#40200D",  # 900
                    "#27180E",  # 950
                ]
            case Theme.FLEXOKI_YELLOW:
                return [
                    "#FAEEC6",  # 50
                    "#F6E2A0",  # 100
                    "#F1D67E",  # 150
                    "#ECCB60",  # 200
                    "#DFB431",  # 300
                    "#D0A215",  # 400
                    "#BE9207",  # 500
                    "#AD8301",  # 600
                    "#8E6B01",  # 700
                    "#664D01",  # 800
                    "#503D02",  # 850
                    "#3A2D04",  # 900
                    "#241E08",  # 950
                ]
            case Theme.FLEXOKI_GREEN:
                return [
                    "#EDEECF",  # 50
                    "#DDE2B2",  # 100
                    "#CDD597",  # 150
                    "#BEC97E",  # 200
                    "#A0AF54",  # 300
                    "#879A39",  # 400
                    "#768D21",  # 500
                    "#66800B",  # 600
                    "#536907",  # 700
                    "#3D4C07",  # 800
                    "#313D07",  # 850
                    "#252D09",  # 900
                    "#1A1E0C",  # 950
                ]
            case Theme.FLEXOKI_CYAN:
                return [
                    "#DDF1E4",  # 50
                    "#BFE8D9",  # 100
                    "#A2DECE",  # 150
                    "#87D3C3",  # 200
                    "#5ABDAC",  # 300
                    "#3AA99F",  # 400
                    "#2F968D",  # 500
                    "#24837B",  # 600
                    "#1C6C66",  # 700
                    "#164F4A",  # 800
                    "#143F3C",  # 850
                    "#122F2C",  # 900
                    "#101F1D",  # 950
                ]
            case Theme.FLEXOKI_BLUE:
                return [
                    "",  # 50
                    "",  # 100
                    "",  # 150
                    "",  # 200
                    "",  # 300
                    "",  # 400
                    "",  # 500
                    "",  # 600
                    "",  # 700
                    "",  # 800
                    "",  # 850
                    "",  # 900
                    "",  # 950
                ]
            case Theme.FLEXOKI_PURPLE:
                return [
                    "",  # 50
                    "",  # 100
                    "",  # 150
                    "",  # 200
                    "",  # 300
                    "",  # 400
                    "",  # 500
                    "",  # 600
                    "",  # 700
                    "",  # 800
                    "",  # 850
                    "",  # 900
                    "",  # 950
                ]
            case Theme.FLEXOKI_MAGENTA:
                return [
                    "",  # 50
                    "",  # 100
                    "",  # 150
                    "",  # 200
                    "",  # 300
                    "",  # 400
                    "",  # 500
                    "",  # 600
                    "",  # 700
                    "",  # 800
                    "",  # 850
                    "",  # 900
                    "",  # 950
                ]
