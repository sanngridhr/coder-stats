from typing import Annotated, TypeAlias

from pydantic import BaseModel, ConfigDict, StringConstraints

HexColour: TypeAlias = Annotated[str, StringConstraints(pattern=r"^#[0-9A-Fa-f{6}$]")]


class Colours(BaseModel):
    model_config = ConfigDict(frozen=True)

    gradient: list[HexColour]
    background: HexColour
    foreground: HexColour
