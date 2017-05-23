from typing import Any

import pytest  # type: ignore

from basic_utils.seq_helpers import (
    butlast,
    cons,
    dedupe,
    first,
    flatten,
    last,
    partial_flatten,
    rest,
    reverse,
    second,
)


@pytest.mark.parametrize("args", [
    ([1, 2, 3]),
    ((1, 2, 3,)),
    (range(1, 4)),
])
def test_first(args: Any) -> None:
    """Tests that first returns the first element in a sequence"""
    assert first(args) == 1


@pytest.mark.parametrize("args", [
    ([1, 2, 3]),
    ((1, 2, 3,)),
    (range(1, 4)),
])
def test_second(args: Any) -> None:
    """Tests that second returns the second element in a sequence"""
    assert second(args) == 2


@pytest.mark.parametrize("args", [
    ([1, 2, 3]),
    ((1, 2, 3,)),
    (range(1, 4)),
])
def test_last(args: Any) -> None:
    """Tests that last returns the last element in a sequence"""
    assert last(args) == 3


@pytest.mark.parametrize("args, expected", [
    ([1, 2, 3], [2, 3]),
    ((1, 2, 3), (2, 3)),
    ((range(1, 4)), range(2, 4)),
])
def test_rest(args: Any, expected: Any) -> None:
    """Tests that rest returns the remaining elements in a sequence"""
    assert rest(args) == expected


@pytest.mark.parametrize("args, expected", [
    ([1, 2, 3], [1, 2]),
    ((1, 2, 3), (1, 2)),
    (range(1, 4), range(1, 3))
])
def test_butlast(args: Any, expected: Any) -> None:
    """Tests that butlast returns all but the last element in a sequence"""
    assert butlast(args) == expected


@pytest.mark.parametrize("args, expected", [
    ('hello world', 'dlrow olleh'),
    ([1, 2, 3], [3, 2, 1]),
    ((1, 2, 3), (3, 2, 1)),
    (range(1, 4), range(3, 0, -1)),
])
def test_reverse(args: Any, expected: Any) -> None:
    assert reverse(args) == expected


@pytest.mark.parametrize("args, expected", [
    ([[1, [2, [3, [4]]]]], [1, 2, 3, 4]),
    ((1, 2, (3, (4,))), [1, 2, 3, 4]),
    (((1,), (2,), (3, 4)), [1, 2, 3, 4])
])
def test_flatten(args: Any, expected: Any) -> None:
    """
    Tests that flatten returns a completely flattened version nested data
    """
    assert list(flatten(args)) == expected


@pytest.mark.parametrize("args, expected", [
    ([[1], [2], [3]], [1, 2, 3]),
    ([[1, 2], [3, 4, 5]], [1, 2, 3, 4, 5]),
    (((1, 2), (3,)), [1, 2, 3]),
])
def test_partial_flatten(args: Any, expected: Any) -> None:
    """
    Tests that partial_flatten returns a partially flattened version data
    """
    assert list(partial_flatten(args)) == expected


@pytest.mark.parametrize("args, expected", [
    (([1, 5, 2, 1, 9, 1, 5, 10], None), [1, 5, 2, 9, 10]),
    ((["jack", "joe", "jay", "ian"], len), ["jack", "joe"])
])
def test_dedupe(args: Any, expected: Any) -> None:
    """Tests that dedupe removes duplicates whilst preserving order"""
    assert list(dedupe(*args)) == expected


@pytest.mark.parametrize("args, expected", [
    ((1, [2, 3]), [1, 2, 3]),
    ((2, [3, 4, 5, 6]), [2, 3, 4, 5, 6]),
])
def test_cons(args: Any, expected: Any) -> None:
    assert list(cons(*args)) == expected
