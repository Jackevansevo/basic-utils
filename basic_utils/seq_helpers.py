from itertools import chain
from typing import Any, Callable, Iterable, Sequence

__all__ = [
    'butlast', 'concat', 'cons', 'dedupe', 'first', 'flatten', 'head', 'init',
    'last', 'partial_flatten', 'rest', 'reverse', 'tail'
]


def first(seq: Sequence) -> Any:
    """
    Returns first element in a sequence.

    >>> first([1, 2, 3])
    1
    """
    return next(iter(seq))


def second(seq: Sequence) -> Any:
    """
    Returns second element in a sequence.

    >>> second([1, 2, 3])
    2
    """
    return seq[1]


def last(seq: Sequence) -> Any:
    """
    Returns the last item in a Sequence

    >>> last([1, 2, 3])
    3
    """
    return seq[-1]


def butlast(seq: Sequence) -> Sequence:
    """
    Returns all but the last item in sequence

    >>> butlast([1, 2, 3])
    [1, 2]
    """
    return seq[:-1]


def rest(seq: Sequence) -> Any:
    """
    Returns remaining elements in a sequence

    >>> rest([1, 2, 3])
    [2, 3]
    """
    return seq[1:]


def reverse(seq: Sequence) -> Sequence:
    """
    Returns sequence in reverse order

    >>> reverse([1, 2, 3])
    [3, 2, 1]
    """
    return seq[::-1]


def cons(item: Any, seq: Sequence) -> chain:
    """ Adds item to beginning of sequence.

    >>> list(cons(1, [2, 3]))
    [1, 2, 3]
    """
    return chain([item], seq)


def flatten(seq: Iterable) -> Iterable:
    """
    Returns a generator object which when evalutated
    returns a flatted version of seq

    >>> list(flatten([1, [2, [3, [4, 5], 6], 7]]))
    [1, 2, 3, 4, 5, 6, 7]
    """
    for item in seq:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item


def partial_flatten(seq: Iterable) -> Iterable:
    """
    Returns partially flattened version of seq

    >>> list(flatten([[1, 2, 3], [4, 5, 6]]))
    [1, 2, 3, 4, 5, 6]
    """
    return chain.from_iterable(seq)


def dedupe(seq: Sequence, key: Callable=None) -> Iterable:
    """
    Removes duplicates from a sequence while maintaining order

    >>> list(dedupe([1, 5, 2, 1, 9, 1, 5, 10]))
    [1, 5, 2, 9, 10]
    """
    seen = set()  # type: set
    for item in seq:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# Define some common aliases
head = first
tail = rest
init = butlast
concat = chain
