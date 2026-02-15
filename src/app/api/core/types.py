from typing import Annotated, Literal

from pydantic import UrlConstraints
from pydantic_core import Url

type EmptyStr = Literal[""]
type SshUrl = Annotated[Url, UrlConstraints(max_length=2083, allowed_schemes=["ssh"])]