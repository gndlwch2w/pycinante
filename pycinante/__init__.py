import sys
import inspect
from types import FunctionType

__all__ = ["export"]
__version__ = "0.0.5rc"

def export(obj=None):
    """
    Exports a function/class/variable definition into its module's `__all__`.

    Examples:
        >>> # the function `f` will be exported into its `__all__`
        >>> @export
        >>> def f(): pass
        >>> # the class `A` will be exported into its `__all__` as well
        >>> @export
        >>> class A(object): pass
        >>> # you also can export a variable into `__all__` as follows
        >>> arr = ...
        >>> export("arr")  # here you need to specify the name of the variable
    """
    if obj is None:
        return export

    if isinstance(obj, str):
        # got module name from the caller is in
        module_name = inspect.currentframe().f_back.f_globals["__name__"]
        module = sys.modules[module_name]
        if obj not in dir(module):
            raise ValueError(f"the object {obj} not found in module {module_name}")
        name = obj
    elif isinstance(obj, (FunctionType, type)):
        # got module name from the object's attributes
        name = obj.__name__
        module = sys.modules[obj.__module__]
    else:
        raise ValueError(f"unsupported type {type(obj)} for exporting")

    if hasattr(module, "__all__"):
        if name not in module.__all__:
            module.__all__.append(name)
    else:
        module.__all__ = [name]

    # return the object itself only when the object is a not str
    if not isinstance(obj, str):
        return obj
