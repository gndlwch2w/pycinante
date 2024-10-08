from __future__ import annotations
from concurrent.futures import Executor
from decimal import Decimal
from requests import Session, Response, PreparedRequest
from requests.auth import AuthBase
from requests.sessions import RequestsCookieJar
from pycinante.io.utils import PathType
from typing import *
from typing_extensions import Self
from _typeshed import SupportsItems, SupportsRead
from pycinante.utils import optional_import

T = TypeVar("T")
E = TypeVar("E")
R = TypeVar("R")
A = TypeVar("A")
U = TypeVar("U")

Predicate: TypeAlias = Callable[[Union[T, Any]], bool]
Supplier: TypeAlias = Callable[[], Union[T, Any]]
Consumer: TypeAlias = Callable[[Union[T, Any]], None]
BiConsumer: TypeAlias = Callable[[Union[T, Any], Union[R, Any]], None]
Function: TypeAlias = Callable[[Union[T, Any]], Union[R, T, Any]]
BiFunction: TypeAlias = Callable[[U, Union[T, Any]], Union[U, Any]]
BinaryOperator: TypeAlias = Callable[[Union[T, Any], Union[R, Any]], Union[R, Any]]

Number: TypeAlias = Union[int, float]
Element: TypeAlias = Union[Iterable[T], Iterator[T], Supplier[Iterable[T]]]
IgnoredExceptions: TypeAlias = Union[Type[Exception], Tuple[Type[Exception], Any]]

# types of requests
Auth: TypeAlias = Union[tuple[str, str], AuthBase, Callable[[PreparedRequest], PreparedRequest]]
Cert: TypeAlias = Union[str, tuple[str, str]]
Data: TypeAlias = (Iterable[bytes] | str | bytes | SupportsRead[str | bytes] | list[tuple[Any, Any]] | tuple[tuple[Any, Any], ...] | Mapping[Any, Any])
_FileName: TypeAlias = str | None
_FileContent: TypeAlias = SupportsRead[str | bytes] | str | bytes
_FileContentType: TypeAlias = str
_FileCustomHeaders: TypeAlias = Mapping[str, str]
_FileSpecTuple2: TypeAlias = tuple[_FileName, _FileContent]
_FileSpecTuple3: TypeAlias = tuple[_FileName, _FileContent, _FileContentType]
_FileSpecTuple4: TypeAlias = tuple[_FileName, _FileContent, _FileContentType, _FileCustomHeaders]
_FileSpec: TypeAlias = _FileContent | _FileSpecTuple2 | _FileSpecTuple3 | _FileSpecTuple4
Files: TypeAlias = Mapping[str, _FileSpec] | Iterable[tuple[str, _FileSpec]]
_Hook: TypeAlias = Callable[[Response], Any]
HooksInput: TypeAlias = Mapping[str, Iterable[_Hook] | _Hook]
_ParamsMappingKeyType: TypeAlias = str | bytes | int | float
_ParamsMappingValueType: TypeAlias = str | bytes | int | float | Iterable[str | bytes | int | float] | None
Params: TypeAlias = Union[
    SupportsItems[_ParamsMappingKeyType, _ParamsMappingValueType],
    tuple[_ParamsMappingKeyType, _ParamsMappingValueType],
    Iterable[tuple[_ParamsMappingKeyType, _ParamsMappingValueType]],
    str | bytes,
]
TextMapping: TypeAlias = MutableMapping[str, str]
Timeout: TypeAlias = Union[float, tuple[float, float], tuple[float, None]]
Verify: TypeAlias = bool | str
HeadersMapping: TypeAlias = Mapping[str, str | bytes]

# bs4
Tag, _ = optional_import(module="bs4", name="Tag")

class Stream(Iterable[E]):
    _element: Element[E] | None
    _executor: Executor

    @staticmethod
    def of(element: Optional[Element[T]] = ..., executor: Optional[Executor] = ..., **kwargs: Any) -> Stream[T]: ...

    @staticmethod
    @overload
    def range(stop: int, executor: Optional[Executor] = ..., **kwargs) -> Stream[int]: ...

    @staticmethod
    @overload
    def range(start: int, stop: int, step: int, executor: Optional[Executor] = ..., **kwargs) -> Stream[int]: ...

    @staticmethod
    def range(*args: int, executor: Optional[Executor] = ..., **kwargs: Any) -> Stream[int]: ...

    @staticmethod
    def concat(*streams: Stream[T], executor: Optional[Executor] = ..., **kwargs: Any) -> Stream[T]: ...

    @staticmethod
    def load(path: PathType, loader: Optional[Callable[[PathType, Any], T]] = ..., executor: Optional[Executor] = ..., **kwargs: Any) -> Stream[T]: ...

    def __init__(self, element: Element[E] | None = ..., executor: Optional[Executor] = ..., **kwargs: Any) -> ...: ...

    @property
    def _copy_element(self) -> Iterator[E]: ...

    # map #

    def map(
        self,
        mapper: Function[E, R],
        parallel: bool = False,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...,
    ) -> Stream[R]: ...

    def map_by_index(
        self,
        index: int,
        mapper: Function[E, E],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def map_key(
        self,
        mapper: Function[E, E],
        default_index: int = ...,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def map_value(
        self,
        mapper: Function[E, E],
        default_index: int = ...,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def keys(
        self,
        default_index: int = ...,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[R]: ...

    def values(
        self,
        default_index: int = ...,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[R]: ...

    def enumerate(self, start: int = ..., parallel: bool = ..., **kwargs: Any) -> Stream[Tuple[int, E]]: ...

    def flatten(self, parallel: bool = ..., **kwargs: Any) -> Stream[R]: ...

    def group_by(self, key: Callable[[E], R], parallel: bool = ..., **kwargs: Any) -> Stream[Tuple[R, Iterable[E]]]: ...

    def zip(self, parallel: bool = ..., **kwargs: Any) -> Stream[Tuple[E]]: ...

    def product(self, repeat: int = ..., parallel: bool = ..., **kwargs: Any) -> Stream[Tuple[E]]: ...

    def int(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[int]: ...

    def float(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[float]: ...

    def decimal(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[Decimal]: ...

    def str(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[str]: ...

    def format(
        self,
        template: str,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[str]: ...

    # # map / requests

    def request(
        self,
        method: str | bytes,
        parallel: bool = ...,
        session: Optional[Session] = ...,
        ignored: Optional[IgnoredExceptions] = ...,
        handler: Optional[Function[IgnoredExceptions, Optional[E]]] = ...,
        *,
        params: Params | None = ...,
        data: Data | None = ...,
        headers: HeadersMapping | None = ...,
        cookies: RequestsCookieJar | TextMapping | None = ...,
        files: Files | None = ...,
        auth: Auth | None = ...,
        timeout: Timeout | None = ...,
        allow_redirects: bool = ...,
        proxies: TextMapping | None = ...,
        hooks: HooksInput | None = ...,
        stream: bool | None = ...,
        verify: Verify | None = ...,
        cert: Cert | None = ...,
        json: Any | None = ...,
        exc_params: Dict[str, Any] | None = None
    ) -> Stream[Response]: ...

    def get(
        self,
        params: Optional[Dict[str, Any]] = ...,
        parallel: bool = ...,
        session: Optional[Session] = ...,
        ignored: Optional[IgnoredExceptions] = ...,
        handler: Optional[Function[IgnoredExceptions, Optional[E]]] = ...,
        *,
        data: Data | None = ...,
        headers: HeadersMapping | None = ...,
        cookies: RequestsCookieJar | TextMapping | None = ...,
        files: Files | None = ...,
        auth: Auth | None = ...,
        timeout: Timeout | None = ...,
        allow_redirects: bool = ...,
        proxies: TextMapping | None = ...,
        hooks: HooksInput | None = ...,
        stream: bool | None = ...,
        verify: Verify | None = ...,
        cert: Cert | None = ...,
        json: Any | None = ...,
        exc_params: Dict[str, Any] | None = None
    ) -> Stream[Response]: ...

    def post(
        self,
        data: Data | None = ...,
        json: Any | None = ...,
        parallel: bool = ...,
        session: Optional[Session] = ...,
        ignored: Optional[IgnoredExceptions] = ...,
        handler: Optional[Function[IgnoredExceptions, Optional[E]]] = ...,
        *,
        params: Params | None = ...,
        headers: HeadersMapping | None = ...,
        cookies: RequestsCookieJar | TextMapping | None = ...,
        files: Files | None = ...,
        auth: Auth | None = ...,
        timeout: Timeout | None = ...,
        allow_redirects: bool = ...,
        proxies: TextMapping | None = ...,
        hooks: HooksInput | None = ...,
        stream: bool | None = ...,
        verify: Verify | None = ...,
        cert: Cert | None = ...,
        exc_params: Dict[str, Any] | None = None
    ) -> Stream[Response]: ...

    def json(
        self,
        parallel: bool = False,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[R]: ...

    def soup(
        self,
        parallel: bool = False,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[Tag]: ...

    # filter #

    def filter(
        self,
        predicate: Predicate[E],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def include(
        self,
        predicate: Predicate[E],
        parallel: bool = ..., *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def exclude(
        self,
        predicate: Predicate[E],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def regexp(
        self,
        pattern: str,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def even(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def odd(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def divisible_by(
        self,
        number: Number,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def distinct(self, key: Function[E, R] = ..., parallel: bool = ..., **kwargs: Any) -> Stream[E]: ...

    def instance_of(
        self,
        types: Type | Tuple[Type],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def no_none(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def no_false(
        self,
        default: Predicate[E] = bool,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def limit(self, max_size: int, parallel: bool = ..., **kwargs: Any) -> Self: ...

    def skip(self, n: int, parallel: bool = ..., **kwargs: Any) -> Stream[E]: ...

    def first(
        self,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Optional[E]: ...

    def last(self, parallel: bool = ..., **kwargs: Any) -> Optional[E]: ...

    def take(self, index: int, parallel: bool = ..., **kwargs: Any) -> Optional[E]: ...

    # collect #

    def collect(
        self,
        supplier: Supplier[A | R],
        accumulator: BiConsumer[A | R, E],
        finisher: Function[A | R, R] = ...,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> R: ...

    def tuplify(self, parallel: bool = ..., **kwargs: Any) -> Tuple[E]: ...

    def listify(self, parallel: bool = ..., **kwargs: Any) -> List[E]: ...

    def setify(self, parallel: bool = ..., **kwargs: Any) -> Set[E]: ...

    def dictify(self, parallel: bool = ..., **kwargs: Any) -> Dict[Any, Any]: ...

    # reduce #

    def reduce(self, accumulator: BinaryOperator[E], e: E = ..., parallel: bool = ..., **kwargs: Any) -> Optional[E]: ...

    def any(
        self,
        predicate: Predicate[E],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> bool: ...

    def all(
        self,
        predicate: Predicate[E],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> bool: ...

    def count(self, parallel: bool = ..., **kwargs: Any) -> int: ...

    def sum(self, parallel: bool = ..., **kwargs: Any) -> Optional[E]: ...

    def mean(self, parallel: bool = ..., **kwargs: Any) -> Optional[E]: ...

    def min(self, key: Function[E, R] = ..., parallel: bool = ..., **kwargs: Any) -> Optional[E]: ...

    def max(self, key: Function[E, R] = ..., parallel: bool = ..., **kwargs: Any) -> Optional[E]: ...

    def join(
        self,
        sep: str = ...,
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> E: ...

    # order #

    def reorder(self, orders: Iterable[int], parallel: bool = ..., **kwargs: Any) -> Stream[E]: ...

    def sort(self, key: Function[E, R] = ..., ascending: bool = True, parallel: bool = ..., **kwargs: Any) -> Stream[E]: ...

    def reverse(self, parallel: bool = ..., **kwargs: Any) -> Stream[E]: ...

    def shuffle(self, parallel: bool = ..., **kwargs: Any) -> Stream[E]: ...

    # traverse #

    def peek(
        self,
        action: Consumer[E],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> Stream[E]: ...

    def foreach(
        self,
        action: Consumer[E],
        parallel: bool = ...,
        *,
        ignored: IgnoredExceptions | None = None,
        handler: Function[IgnoredExceptions, R] | None = None,
        executor: Executor | None = None,
        # below arguments only when parallel=True and executor=None works
        io_intensive: bool = True,
        thread_name_prefix: str | None = "",
        initializer: Callable[..., object] | None = ...,
        initargs: tuple[Any, ...] = ...
    ) -> ...: ...

    # misc #

    def __len__(self) -> int: ...

    def __getitem__(self, index: int | slice) -> E | Stream[E]: ...

    def __iter__(self) -> Iterator[E]: ...

stream: Type[Stream]
