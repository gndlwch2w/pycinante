"""Update Log

2024.10.07:
    - completely tested attrdict and attrify()'s functionalities provided already
    - added the generic supports for any type of inputs
    - fixed the __dir__() method returning duplicate attributes
    - fixed a bug where the __getitem__() method do not raise a KeyError when accessing no-exists keys
    - added a feature to pop() method that allows elements to be pop via chain keys
    - added the supports to other methods in dict (and not in attrdict before)
"""

from __future__ import annotations
import contextlib
from pycinante.dict.utils import *
from typing import TypeVar, Dict, Optional, Iterable, Union, Any, Tuple
from typing_extensions import Self

__all__ = ["attrdict", "attrify"]

_E = TypeVar("_E")
E = Union[_E, Any]

T = TypeVar("T")
Element = Optional[Union[Dict[str, T], Iterable[Iterable]]]

class AttrDict(Dict[str, E]):
    """Attribute dictionary, allowing access to dict values as if they were class attributes.

    Using cases:
        >>> net = attrdict({"name": "unet", "cfg": {"in_channels": 3, "num_classes": 9}})
        >>> net.cfg.num_classes
        9
        >>> net["cfg.decoder.depths"] = [2, 2, 2, 2]
        >>> net["cfg.decoder.depths"][0]
        2

        As shown above, you first need to covert an existing dict into AttrDict, and then you can access its value as
        you access a class/instance's properties. Moreover, you can get/set the value in `[]` via cascaded strings.
    """
    def __init__(self, seq: Element[E] = None, **kwargs: E) -> None:
        super(AttrDict, self).__init__()
        self.update(seq, **kwargs)

    def clear(self) -> Self:
        """
        Remove all items from the dictionary. Return itself. Note that the clear() function only deletes references to
        currently held instances.
        """
        _ = [delattr(self, key) for key in self.keys()]
        super(AttrDict, self).clear()
        return self

    def copy(self) -> AttrDict[E]:
        """
        Return a shallow copy of the current instance.
        """
        return AttrDict(super(AttrDict, self).copy())

    @staticmethod
    def fromkeys(iterable: Iterable[str], values: Optional[E] = None, **_kwargs: Any) -> AttrDict[E]:
        """
        Create a new dictionary with keys from iterable and values set to value.
        """
        return AttrDict(dict.fromkeys(iterable, values))

    def get(self, key: str, default: Optional[E] = None) -> E:
        """
        Return the value for key if key is in the dictionary, else default.
        """
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def items(self) -> dict_items[str, E]:
        """
        Return a new view of the dictionary’s items ((key, value) pairs).
        """
        return super(AttrDict, self).items()

    def keys(self) -> dict_keys[str]:
        """
        Return a new view of the dictionary’s keys.
        """
        return super(AttrDict, self).keys()

    def pop(self, key: str, default: Optional[E] = None) -> E:
        """
        If key is in the dictionary, remove it and return its value, else return default. If default is not given and
        key is not in the dictionary, a KeyError is raised.
        """
        if "." in key:
            prefix, key = key.rsplit(sep=".", maxsplit=1)
            parent = self.__getitem__(prefix)
        else:
            parent = self

        with contextlib.suppress(AttributeError):
            delattr(parent, key)
        return super(AttrDict, parent).pop(key, default)

    def popitem(self) -> Tuple[str, E]:
        """
        Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.
        """
        ret = super(AttrDict, self).popitem()
        with contextlib.suppress(AttributeError):
            delattr(self, ret[0])
        return ret

    def setdefault(self, key: str, default: Optional[E] = None) -> E:
        """
        If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
        default defaults to None.
        """
        if self.__contains__(key):
            return self.__getitem__(key)
        self.__setitem__(key, default)
        return default

    def update(self, seq: Element[E] = None, **kwargs: E) -> Self:
        """
        Update the dictionary with the key/value pairs from other, overwriting existing keys. Return itself.
        """
        for key, value in dict(seq or {}, **kwargs).items():
            self.__setattr__(key, value)
        return self

    def values(self) -> dict_values[E]:
        """
        Return a new view of the dictionary’s values.
        """
        return super(AttrDict, self).values()

    def __contains__(self, key: str) -> bool:
        """
        Return True if the dictionary has the specified key, else False.
        """
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def __delitem__(self, key: str) -> None:
        """
        Delete self[key]. It is implemented by pop().
        """
        self.pop(key)

    def __setattr__(self, key: str, value: E) -> None:
        """
        Set d[key]=value and at same time set d.key=value.
        """
        def _covert_recursively(obj: E) -> E:
            if isinstance(obj, dict) and not isinstance(obj, AttrDict):
                return self.__class__(obj)
            if isinstance(obj, (tuple, list, set)):
                return type(obj)((_covert_recursively(e) for e in obj))
            return obj

        value = _covert_recursively(value)
        super(AttrDict, self).__setattr__(key, value)
        super(AttrDict, self).__setitem__(key, value)

    def __getattr__(self, key: str) -> E:
        """
        Return the value for key if key is in the dictionary, else raise a KeyError.
        """
        return super(AttrDict, self).__getitem__(key)

    def __setitem__(self, key: str, value: E) -> None:
        """
        It works similar to __setattr__(), and you can set key/value pair in str chain way like d["a.b.c.d"]=value.
        """
        if "." in key:
            key, suffix = key.split(sep=".", maxsplit=1)
            self.__setattr__(key, value={}) if key not in self else None
            self.__getattr__(key).__setitem__(suffix, value)
        else:
            self.__setattr__(key, value)

    def __getitem__(self, key: str) -> E:
        """
        It works similar to __getattr__(), and you can get key/value pair in str chain way like d["a.b.c.d"].
        """
        if "." in key:
            prefix, key = key.rsplit(sep=".", maxsplit=1)
            d = self.__getitem__(prefix)
            if not isinstance(d, AttrDict):
                raise KeyError(".".join((prefix, key)))
            return d[key]
        return self.__getattr__(key)

    def __dir__(self) -> Iterable[str]:
        """
        Return all method/attribute names of the instance.
        """
        return super(AttrDict, self).__dir__()

def attrify(seq: Element[T] = None, **kwargs: T) -> AttrDict[T]:
    """
    Covert a dict/iterable into a AttrDict.
    """
    return AttrDict(seq, **kwargs)

attrdict = AttrDict
