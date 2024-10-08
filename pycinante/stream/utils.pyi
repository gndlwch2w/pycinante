from concurrent.futures import Executor
from typing import Any, Callable, Iterable, Iterator, TypeVar
from pycinante.stream.pystream import Predicate, Supplier, Consumer, Function, Element, IgnoredExceptions

T = TypeVar('T')
R = TypeVar('R')
U = TypeVar('U')

def get_executor(
    max_workers: int | None = None,
    io_intensive: bool = True,
    *,
    thread_name_prefix: str | None = "",
    initializer: Callable[..., object] | None = ...,
    initargs: tuple[Any, ...] = ...,
) -> Executor: ...

def concrt_map(
    func: Function[T, R],
    iters: Iterable[T],
    *,
    executor: Executor | None = None,
    io_intensive: bool = True,
    thread_name_prefix: str | None = "",
    initializer: Callable[..., object] | None = ...,
    initargs: tuple[Any, ...] = ...,
) -> Iterable[R]: ...

def concrt_filter(
    func: Predicate[T],
    iters: Iterable[T],
    *,
    executor: Executor | None = None,
    io_intensive: bool = True,
    thread_name_prefix: str | None = "",
    initializer: Callable[..., object] | None = ...,
    initargs: tuple[Any, ...] = ...,
) -> Iterable[T]: ...

class MemoryBuffer(Iterable[T]):
    _elements: Element[T] | None
    def __init__(self, element: Element[T] | None = None) -> None: ...
    def __iter__(self) -> Iterator[T]: ...

def try_catch(ignored: IgnoredExceptions = ..., val: T | None = None, name: str = 'other') -> Callable[..., T | None]: ...

def identity(*args: T, **kwargs: T) -> T | tuple[T] | dict[str, T]: ...

def distinct(iterable: Iterable[T], key: Function[T, R] | None = None) -> Iterator[T]: ...

def bool_plus(obj: Any, default: Callable[[Any], bool] = ...) -> bool: ...

def flatten(iterable: Iterable[T | Iterable[T]]) -> Iterator[T]: ...

def conditional_warning(condition: bool, msg: str = '', **kwargs: Any) -> None: ...

def reorder(iterables: Iterable[T], orders: Iterable[int]) -> Iterator[T]: ...

def shuffle(iterables: Iterable[T]) -> Iterator[T]: ...

def peek(element: T, func: Consumer[T]) -> T: ...

def group_by(iterable: Iterable[T], key: Function[T, R] = ...) -> Iterator[tuple[R, Iterable[T]]]: ...

def parallel_warning(parallel: bool, **kwargs: Any) -> None: ...

def cartesian_product(iterable: Iterable[T], repeat: int = 1) -> Iterator[T]: ...

def get_el_by_index(iterable: Iterable[T], index: int) -> T: ...

def supress(func: Supplier[T], ignored: IgnoredExceptions, handler: Function[IgnoredExceptions, T | None] | None = None) -> R | None: ...

def format(obj: Any, template: str) -> str: ...
