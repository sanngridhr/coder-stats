from enum import StrEnum
from typing import Self

from app.api.core.theme.models.template import Colours, HexColour


class Theme(StrEnum):
    """
    Some themes are included under the MIT license:

    Copyright (c) 2023 Steph Ango
    """

    colours: Colours

    FLEXOKI_DARK = (
        "flexoki-dark",
        Colours(
            background="#100F0F",
            foreground="#CECDC3",
            gradient=[
                "#D14D41",
                "#DA702C",
                "#D0A215",
                "#879A39",
                "#3AA99F",
                "#4385BE",
                "#8B7EC8",
                "#CE5D97",
            ],
        ),
    )
    FLEXOKI_LIGHT = (
        "flexoki-light",
        Colours(
            background="#FFFCF0",
            foreground="#100F0F",
            gradient=[
                "#AF3029",
                "#BC5215",
                "#AD8301",
                "#66800B",
                "#24837B",
                "#205EA6",
                "#5E409D",
                "#A02F6F",
            ],
        ),
    )
    FLEXOKI_BASE = (
        "flexoki-base",
        Colours(
            background="#F2F0E5",
            foreground="#1C1B1A",
            gradient=[
                "#E6E4D9",
                "#DAD8CE",
                "#CECDC3",
                "#B7B5AC",
                "#9F9D96",
                "#878580",
                "#6F6E69",
                "#575653",
                "#403E3C",
                "#343331",
                "#282726",
            ],
        ),
    )
    FLEXOKI_RED = (
        "flexoki-red",
        Colours(
            background="#FFE1D5",
            foreground="#261312",
            gradient=[
                "#FFCABB",
                "#FDB2A2",
                "#F89A8A",
                "#E8705F",
                "#D14D41",
                "#C03E35",
                "#AF3029",
                "#942822",
                "#6C201C",
                "#551B18",
                "#3E1715",
            ],
        ),
    )
    FLEXOKI_ORANGE = (
        "flexoki-orange",
        Colours(
            background="#FFE7CE",
            foreground="#27180E",
            gradient=[
                "#FED3AF",
                "#FCC192",
                "#F9AE77",
                "#EC8B49",
                "#DA702C",
                "#CB6120",
                "#BC5215",
                "#9D4310",
                "#71320D",
                "#59290D",
                "#40200D",
            ],
        ),
    )
    FLEXOKI_YELLOW = (
        "flexoki-yellow",
        Colours(
            background="#FAEEC6",
            foreground="#241E08",
            gradient=[
                "#F6E2A0",
                "#F1D67E",
                "#ECCB60",
                "#DFB431",
                "#D0A215",
                "#BE9207",
                "#AD8301",
                "#8E6B01",
                "#664D01",
                "#503D02",
                "#3A2D04",
            ],
        ),
    )
    FLEXOKI_GREEN = (
        "flexoki-green",
        Colours(
            background="#EDEECF",
            foreground="#1A1E0C",
            gradient=[
                "#DDE2B2",
                "#CDD597",
                "#BEC97E",
                "#A0AF54",
                "#879A39",
                "#768D21",
                "#66800B",
                "#536907",
                "#3D4C07",
                "#313D07",
                "#252D09",
            ],
        ),
    )
    FLEXOKI_CYAN = (
        "flexoki-cyan",
        Colours(
            background="#DDF1E4",
            foreground="#101F1D",
            gradient=[
                "#BFE8D9",
                "#A2DECE",
                "#87D3C3",
                "#5ABDAC",
                "#3AA99F",
                "#2F968D",
                "#24837B",
                "#1C6C66",
                "#164F4A",
                "#143F3C",
                "#122F2C",
            ],
        ),
    )
    FLEXOKI_BLUE = (
        "flexoki-blue",
        Colours(
            background="#E1ECEB",
            foreground="#101A24",
            gradient=[
                "#C6DDE8",
                "#ABCFE2",
                "#92BFDB",
                "#66A0C8",
                "#4385BE",
                "#3171B2",
                "#205EA6",
                "#1A4F8C",
                "#163B66",
                "#133051",
                "#12253B",
            ],
        ),
    )
    FLEXOKI_PURPLE = (
        "flexoki-purple",
        Colours(
            background="#F0EAEC",
            foreground="#1A1623",
            gradient=[
                "#E2D9E9",
                "#D3CAE6",
                "#C4B9E0",
                "#A699D0",
                "#8B7EC8",
                "#735EB5",
                "#5E409D",
                "#4F3685",
                "#3C2A62",
                "#31234E",
                "#261C39",
            ],
        ),
    )
    FLEXOKI_MAGENTA = (
        "flexoki-magenta",
        Colours(
            background="#FEE4E5",
            foreground="#24131D",
            gradient=[
                "#FCCFDA",
                "#F9B9CF",
                "#F4A4C2",
                "#E47DA8",
                "#CE5D97",
                "#B74583",
                "#A02F6F",
                "#87285E",
                "#641F46",
                "#4F1B39",
                "#39172B",
            ],
        ),
    )

    def __new__(cls, name: str, colours: Colours) -> Self:
        obj = str.__new__(cls, name)
        obj._value_ = name
        obj.colours = colours
        return obj

    @property
    def background(self) -> HexColour:
        return self.colours.background

    @property
    def foreground(self) -> HexColour:
        return self.colours.foreground

    @property
    def gradient(self) -> list[HexColour]:
        return self.colours.gradient
