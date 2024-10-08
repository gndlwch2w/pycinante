from logging import Handler
from asyncio import AbstractEventLoop
from datetime import time, timedelta
from multiprocessing.context import BaseContext as Context
from loguru import Writable, Message, PathLikeStr, Record, Logger, Catcher, Contextualizer, Level, LevelConfig
from pycinante.io.utils import PathType
from typing import (
    Callable, TypeVar, Any, Dict, Union, TextIO, List, Awaitable, Type, Optional, Tuple, overload, Literal, IO, AnyStr,
    Sequence, Pattern, Generator, BinaryIO
)
from types import TracebackType

# typing of loguru
F = TypeVar("F", bound=Callable[..., Any])
FilterDict = Dict[Union[str, None], Union[str, int, bool]]
FilterFunction = Callable[[Record], bool]
FormatFunction = Callable[[Record], str]
PatcherFunction = Callable[[Record], None]
RotationFunction = Callable[[Message, TextIO], bool]
RetentionFunction = Callable[[List[str]], None]
CompressionFunction = Callable[[str], None]
AwaitableCompleter = Awaitable[None]
ExcInfo = Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]]
ActivationConfig = Tuple[Union[str, None], bool]

def log(msg: Any, *msgs: Any, level: str, sep: str = " ", prettify: Callable[[Any], str] = ..., **kwargs: Any) -> None: ...

class logger:
    TRACE: int
    DEBUG: int
    INFO: int
    SUCCESS: int
    WARNING: int
    ERROR: int
    CRITICAL: int

    @staticmethod
    @overload
    def trace(msg: str) -> None: ...

    @staticmethod
    @overload
    def trace(msg: str, *msgs: str) -> None: ...

    @staticmethod
    @overload
    def trace(msg: str, *msgs: str, **kwargs: Any) -> None: ...

    @staticmethod
    def trace(msg: str, *msgs: str, sep: str = " ", prettify: bool = False, **kwargs: Any) -> None: ...

    @staticmethod
    @overload
    def debug(msg: str) -> None: ...

    @staticmethod
    @overload
    def debug(msg: str, *msgs: str) -> None: ...

    @staticmethod
    @overload
    def debug(msg: str, *msgs: str, **kwargs: Any) -> None: ...

    @staticmethod
    def debug(msg: str, *msgs: str, sep: str = " ", prettify: bool = False, **kwargs: Any) -> None: ...

    @staticmethod
    @overload
    def info(msg: str) -> None: ...

    @staticmethod
    @overload
    def info(msg: str, *msgs: str) -> None: ...

    @staticmethod
    @overload
    def info(msg: str, *msgs: str, **kwargs: Any) -> None: ...

    @staticmethod
    def info(msg: str, *msgs: str, sep: str = " ", prettify: bool = False, **kwargs: Any) -> None: ...

    @staticmethod
    @overload
    def success(msg: str) -> None: ...

    @staticmethod
    @overload
    def success(msg: str, *msgs: str) -> None: ...

    @staticmethod
    @overload
    def success(msg: str, *msgs: str, **kwargs: Any) -> None: ...

    @staticmethod
    def success(msg: str, *msgs: str, sep: str = " ", prettify: bool = False, **kwargs: Any) -> None: ...

    @staticmethod
    @overload
    def warning(msg: str) -> None: ...

    @staticmethod
    @overload
    def warning(msg: str, *msgs: str) -> None: ...

    @staticmethod
    @overload
    def warning(msg: str, *msgs: str, **kwargs: Any) -> None: ...

    @staticmethod
    def warning(msg: str, *msgs: str, sep: str = " ", prettify: bool = False, **kwargs: Any) -> None: ...

    @staticmethod
    @overload
    def error(msg: str) -> None: ...

    @staticmethod
    @overload
    def error(msg: str, *msgs: str) -> None: ...

    @staticmethod
    @overload
    def error(msg: str, *msgs: str, **kwargs: Any) -> None: ...

    @staticmethod
    def error(msg: str, *msgs: str, sep: str = " ", prettify: bool = False, **kwargs: Any) -> None: ...

    @staticmethod
    @overload
    def critical(msg: str) -> None: ...

    @staticmethod
    @overload
    def critical(msg: str, *msgs: str) -> None: ...

    @staticmethod
    @overload
    def critical(msg: str, *msgs: str, **kwargs: Any) -> None: ...

    @staticmethod
    def critical(msg: str, *msgs: str, sep: str = " ", prettify: bool = False, **kwargs: Any) -> None: ...

    @staticmethod
    def add(
        sink: Union[TextIO, Writable, Callable[[Message], None], Handler] | Callable[[Message], Awaitable[None]] | Union[str, PathLikeStr],
        *,
        level: int | Literal["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"] = "DEBUG",
        format: Union[str, FormatFunction] = ...,
        filter: Optional[Union[str, FilterFunction, FilterDict]] = None,
        colorize: bool | None = None,
        serialize: bool = False,
        backtrace: bool = True,
        diagnose: bool = True,
        enqueue: bool = False,
        context: Context | str | None = None,
        catch: bool = True,
        # the sink is a coroutine function
        loop: AbstractEventLoop | None = ...,
        # the sink is a file path
        rotation: Optional[Union[str, int, time, timedelta, RotationFunction]] = None,
        retention: Optional[Union[str, int, timedelta, RetentionFunction]] = None,
        compression: Optional[Union[str, CompressionFunction]] = None,
        delay: bool = False,
        watch: bool = False,
        mode: str = "a",
        buffering: int = 1,
        encoding: str = "utf-8",
        **kwargs: Any
    ) -> int: ...

    @staticmethod
    def remove(handler_id: int | IO[AnyStr] | str | None = None) -> None: ...

    @staticmethod
    def complete(**kwargs: Any) -> AwaitableCompleter: ...

    @staticmethod
    @overload
    def catch(exception: F) -> F: ...

    @staticmethod
    def catch(
        exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]] = ...,
        *,
        level: Union[str, int] = ...,
        reraise: bool = ...,
        onerror: Optional[Callable[[BaseException], None]] = ...,
        exclude: Optional[Union[Type[BaseException], Tuple[Type[BaseException], ...]]] = ...,
        default: Any = ...,
        message: str = ...
    ) -> Catcher: ...

    @staticmethod
    def opt(
        *,
        exception: Optional[Union[bool, ExcInfo, BaseException]] = ...,
        record: bool = ...,
        lazy: bool = ...,
        colors: bool = ...,
        raw: bool = ...,
        capture: bool = ...,
        depth: int = ...,
        ansi: bool = ...
    ) -> Logger: ...

    @staticmethod
    def bind(**kwargs: Any) -> Logger: ...

    @staticmethod
    def contextualize(**kwargs: Any) -> Contextualizer: ...

    @staticmethod
    def patch(patcher: PatcherFunction) -> Logger: ...

    @staticmethod
    @overload
    def level(name: str) -> Level: ...

    @staticmethod
    @overload
    def level(
        name: str,
        no: int = ..., color:
        Optional[str] = ...,
        icon: Optional[str] = ...
    ) -> Level: ...

    @staticmethod
    def level(
        name: str,
        no: Optional[int] = ...,
        color: Optional[str] = ...,
        icon: Optional[str] = ...,
    ) -> Level: ...

    @staticmethod
    def disable(name: Union[str, None]) -> None: ...

    @staticmethod
    def enable(name: Union[str, None]) -> None: ...

    @staticmethod
    def configure(
        *,
        handlers: Sequence[Dict[str, Any]] = ...,
        levels: Optional[Sequence[LevelConfig]] = ...,
        extra: Optional[Dict[Any, Any]] = ...,
        patcher: Optional[PatcherFunction] = ...,
        activation: Optional[Sequence[ActivationConfig]] = ...
    ) -> List[int]: ...

    @staticmethod
    @overload
    def parse(
        file: Union[str, PathLikeStr, TextIO],
        pattern: Union[str, Pattern[str]],
        *,
        cast: Union[Dict[str, Callable[[str], Any]], Callable[[Dict[str, str]], None]] = ...,
        chunk: int = ...
    ) -> Generator[Dict[str, Any], None, None]: ...

    @staticmethod
    def parse(
        file: BinaryIO,
        pattern: Union[bytes, Pattern[bytes]],
        *,
        cast: Union[Dict[str, Callable[[bytes], Any]], Callable[[Dict[str, bytes]], None]] = ...,
        chunk: int = ...
    ) -> Generator[Dict[str, Any], None, None]: ...

    @staticmethod
    @overload
    def exception(__message: str, *args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def exception(__message: Any) -> None: ...  # noqa: N805

    @staticmethod
    @overload
    def log(__level: Union[int, str], __message: str, *args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def log(__level: Union[int, str], __message: Any) -> None: ...

    @staticmethod
    def start(*args: Any, **kwargs: Any) -> int: ...

    @staticmethod
    def stop(*args: Any, **kwargs: Any) -> None: ...

    @staticmethod
    def console(
        level: int | Literal["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"] | None = None,
        format: Union[str, FormatFunction] | None = None,
        *,
        filter: Optional[Union[str, FilterFunction, FilterDict]] = None,
        colorize: bool | None = None,
        serialize: bool = False,
        backtrace: bool = True,
        diagnose: bool = True,
        enqueue: bool = False,
        context: Context | str | None = None,
        catch: bool = True,
        # the sink is a coroutine function
        loop: AbstractEventLoop | None = ...,
        # the sink is a file path
        rotation: Optional[Union[str, int, time, timedelta, RotationFunction]] = None,
        retention: Optional[Union[str, int, timedelta, RetentionFunction]] = None,
        compression: Optional[Union[str, CompressionFunction]] = None,
        delay: bool = False,
        watch: bool = False,
        mode: str = "a",
        buffering: int = 1,
        encoding: str = "utf-8",
        **kwargs: Any
    ) -> None: ...

    @staticmethod
    def load_cfg(path: PathType, context: Dict[str, Any] | None = None) -> None: ...
