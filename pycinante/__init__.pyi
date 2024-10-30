from typing import Type, List, overload, Any, Optional
from types import FunctionType

__all__: List[str]
__version__: str

@overload
def export(obj: Optional[str] = ...) -> None: ...
@overload
def export(obj: Optional[Type[Any]] = ...) -> Type[Any]: ...
@overload
def export(obj: Optional[FunctionType] = ...) -> FunctionType: ...
