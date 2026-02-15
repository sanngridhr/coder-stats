from typing import Annotated, Literal

from pydantic import UrlConstraints
from pydantic_core import Url

type EmptyStr = Literal[""]
type SshUrl = Annotated[Url, UrlConstraints(allowed_schemes=["ssh"])]
type GitUrl = Annotated[Url, UrlConstraints(allowed_schemes=["git"])]
