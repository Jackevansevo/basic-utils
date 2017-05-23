from functools import reduce
from operator import getitem
from typing import Any, Callable, Sequence, Tuple

from basic_utils.seq_helpers import butlast, last


__all__ = [
    'dict_subset', 'get_in_dict', 'get_keys', 'prune_dict', 'set_in_dict',
]


def get_keys(d: dict, keys: Sequence[str], default: Callable=None) -> Tuple:
    """
    Returns multiple values for keys in a dictionary

    Empty key values will be None by default

    >>> d = {'x': 24, 'y': 25}
    >>> get_keys(d, ('x', 'y', 'z'))
    (24, 25, None)
    """
    return tuple(d.get(key, default) for key in keys)


def dict_subset(d, keys, prune=False, default=None):
    # type: (dict, Sequence[str], bool, Callable) -> dict
    """
    Returns a new dictionary with a subset of key value pairs from the original

    >>> d = {'a': 1, 'b': 2}
    >>> dict_subset(d, ('c',), True, 'missing')
    {'c': 'missing'}
    """
    new = {k: d.get(k, default) for k in keys}
    if prune:
        return prune_dict(new)
    return new


def get_in_dict(d: dict, keys: Sequence[str]) -> Any:
    """
    Retrieve nested key from dictionary

    >>> d = {'a': {'b': {'c': 3}}}
    >>> get_in_dict(d, ('a', 'b', 'c'))
    3
    """
    return reduce(getitem, keys, d)


def set_in_dict(d: dict, keys: Sequence[str], value: Any) -> None:
    """
    Sets a value inside a nested dictionary

    >>> d = {'a': {'b': {'c': 3}}}
    >>> set_in_dict(d, ('a', 'b', 'c'), 10)
    >>> d
    {'a': {'b': {'c': 10}}}
    """
    get_in_dict(d, butlast(keys))[last(keys)] = value


def prune_dict(d: dict, key: Callable=lambda x: x is not None) -> dict:
    """
    Returns new dictionary with values filtered by key fn.
    Prunes None values by default

    >>> d = {'Homer': 39, 'Marge': 36, 'Bart': 10}
    >>> prune_dict(d, key=lambda x: x < 20)
    {'Bart': 10}
    """
    return {k: v for k, v in d.items() if key(v)}
