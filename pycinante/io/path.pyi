from os import PathLike, path as osp
from pycinante.io.file import File
from pycinante.io.utils import PathType
from typing import Any, AnyStr, Type
from typing_extensions import Self

class Path(PathLike):
    _pathname: AnyStr
    def __init__(self, *pathnames: PathType) -> None: ...
    @property
    def path(self) -> str: ...
    def parent(self) -> Path: ...
    def glob(self, pattern: str, **kwargs: Any) -> list[File | Path]: ...
    def is_dir(self) -> bool: ...
    def is_link(self) -> bool: ...
    def is_mount(self) -> bool: ...
    def is_empty(self) -> bool: ...
    def is_exists(self) -> bool: ...
    def is_not_exists(self) -> bool: ...
    def join(self, *pathnames: PathType) -> Path: ...
    def abs(self) -> Self: ...
    def normcase(self) -> Self: ...
    def normpath(self) -> Self: ...
    def expand_vars(self) -> Self: ...
    def expand_user(self) -> Self: ...
    def relpath(self, start: PathType = ...) -> Self: ...
    def cd(self, dst: PathType) -> Path: ...
    def mkdir(self) -> Self: ...
    def remove(self, **kwargs: Any) -> Self: ...
    def __truediv__(self, pathname: PathType) -> Path: ...
    def __add__(self, name: PathType) -> File: ...
    def __fspath__(self) -> str: ...

path = Type[Path]