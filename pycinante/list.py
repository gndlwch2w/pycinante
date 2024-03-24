"""This module provides functionality for a list object accession.
"""
from __future__ import annotations
from typing import TypeVar, Callable, Any, Iterable, Sequence

__all__ = [
    'is_equal',
    'arange',
    'unique',
    'listify',
    'swap',
    'sort',
    'flatten'
]

T = TypeVar('T')

def is_equal(obj: Any, other: Any) -> bool:
    """Return True if each element of obj and other are equal, False otherwise.

    >>> is_equal(None, None)
    True
    >>> is_equal(None, [1, 2, 3, 4])
    False
    >>> is_equal([1, 2, 3, 4], [1, 2, 3, 4])
    True
    >>> is_equal([1, 2, 3, 4], {1, 2, 3, 4})
    True
    >>> is_equal([4, 5, 6], '456')
    False
    >>> from collections import OrderedDict
    >>> is_equal(OrderedDict.fromkeys(iter([1, 2, 3])).keys(), [1, 2, 3])
    True
    """
    if isinstance(obj, Sequence) and isinstance(other, Sequence):
        if len(obj) != len(other):
            return False
        for a, b in zip(obj, other):
            if a != b:
                return False
        return True
    return obj == other

def listify(obj: ...) -> list[...]:
    """Return a list from an object.

    >>> listify('https://www.baidu.com')
    ['https://www.baidu.com']
    >>> listify([1, 2, 3])
    [1, 2, 3]
    >>> listify((1, 2, 3, 2, 1, 2))
    [1, 2, 3, 2, 1, 2]
    >>> listify(iter({4, 5, 6}))
    [4, 5, 6]
    """
    if isinstance(obj, Iterable) and not isinstance(obj, str):
        return list(obj)
    return [obj]

def arange(start: int = 0, stop: int = None, step: int = 1) -> list[int]:
    """Return a list of numbers between `start` and `stop` inclusive.

    >>> arange(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> arange(1, 10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> arange(49, 200, 40)
    [49, 89, 129, 169]
    """
    return list(range((stop and start) or 0, stop or start, step))

def unique(seq: list[T], key: Callable[[T], bool] = None) -> list[T]:
    """Removes duplicate elements from a list while preserving the order of the rest.

    Args:
        seq (list): list to be removed duplicate elements.
        key (Callable): the value of the optional `key` parameter should be a function
        that takes a single argument and returns a key to test the uniqueness.

    >>> unique([1, 2, 3])
    [1, 2, 3]
    >>> unique([1, 2, 1, 3, 3, 2, 1, 2, 3])
    [1, 2, 3]

    Ref: [1] https://github.com/flaggo/pydu/blob/master/pydu/list.py
    """
    key = key or (lambda e: e)
    unique_seq, seen = list(), set()
    for element in seq:
        if key(element) in seen:
            continue
        unique_seq.append(element)
        seen.add(key(element))
    return unique_seq

def swap(seq: list[T], i: int | slice | Sequence[int], j: int | slice | Sequence[int]) -> list[T]:
    """Swap the element of `arr[i]` and `arr[j] in the list `arr`.

    >>> swap([34, 456, 36, 90, 47], 1, 4)
    [34, 47, 36, 90, 456]
    >>> swap([34, 47, 36, 90, 456], slice(0, 2), slice(2, 4))
    [36, 90, 34, 47, 456]
    >>> swap([43, 68, 25, 99, 23, 83], [1, 2, 3], [0, 5, 4])
    [68, 43, 83, 23, 99, 25]
    """
    assert isinstance(i, type(j)), 'the type of `i` and `j` must be the same'
    if isinstance(i, (int, slice)):
        seq[i], seq[j] = seq[j], seq[i]
        return seq
    assert isinstance(i, Sequence), f'the type of {type(i)} is not supported'
    for m, n in zip(i, j):
        seq[m], seq[n] = seq[n], seq[m]
    return seq

def sort(seq: list[T], descending: bool = False) -> list[T]:
    """Sort the list in-place in ascending or descending order and return itself.

    >>> arr = [34, 456, 36, 90, 47, 34, 55, 999, 323]
    >>> sort(seq, False)
    [34, 34, 36, 47, 55, 90, 323, 456, 999]
    >>> sort(seq, True)
    [999, 456, 323, 90, 55, 47, 36, 34, 34]
    """
    seq.sort(reverse=descending)
    return seq

def flatten(seq: Iterable[Any]) -> list[T]:
    """Generate each element of the given `seq`. If the element is iterable and is not
    string, it yields each sub-element of the element recursively.

    >>> flatten([])
    []
    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([0, [1, 2, 3], [4, 5, 6], [7, [8, [9]]]])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    Ref: [1] https://github.com/flaggo/pydu/blob/master/pydu/list.py
    """
    flatten_seq = []
    for element in seq:
        if (isinstance(element, Iterable) and
                not isinstance(element, (str, bytes))):
            for sub in flatten(element):
                flatten_seq.append(sub)
        else:
            flatten_seq.append(element)
    return flatten_seq
