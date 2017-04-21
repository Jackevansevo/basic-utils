from typing import Any

__all__ = ['dec', 'even', 'identity', 'inc', 'odd']


def identity(x: Any) -> Any:
    """
    Returns the same values passed as arguments

    >>> x = (10, 20)
    >>> identity(x)
    (10, 20)
    """
    return x


def inc(x: int) -> int:
    """
    >>> inc(10)
    11
    """
    return x + 1


def dec(x: int) -> int:
    """
    >>> dec(5)
    4
    """
    return x - 1


def even(x: int) -> bool:
    """
    >>> even(2)
    True
    """
    return x % 2 == 0


def odd(x: int) -> bool:
    """
    >>> even(3)
    False
    """
    return x % 2 == 1
