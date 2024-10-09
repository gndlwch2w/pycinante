from typing import Any, Callable, TypeVar

T = TypeVar("T")

class DeprecatedError(Exception): ...

def deprecated(
    since: str | None = None,
    removed: str | None = None,
    crt_version: str | None = None,
    msg_suffix: str = "",
    warning_category: type[FutureWarning] | None = ...
) -> Callable[..., Any]: ...

def deprecated_arg(
    name: str,
    since: str | None = None,
    removed: str | None = None,
    crt_version: str | None = None,
    msg_suffix: str = '',
    new_name: str | None = None,
    warning_category: type[FutureWarning] | None = ...
) -> Callable[..., Any]: ...

def deprecated_arg_default(
    name: str,
    new_default: Any,
    since: str | None = None,
    replaced: str | None = None,
    crt_version: str | None = None,
    msg_suffix: str = '',
    warning_category: type[FutureWarning] | None = ...
) -> Callable[..., Any]: ...
