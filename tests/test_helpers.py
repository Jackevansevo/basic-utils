from typing import Any

import pytest  # type: ignore

from basic_utils.helpers import (
    butlast,
    cons,
    dedupe,
    dict_subset,
    first,
    flatten,
    get_in_dict,
    get_keys,
    last,
    partial_flatten,
    prune_dict,
    rest,
    reverse,
    set_in_dict
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


@pytest.mark.parametrize("keys, expected, default", [
    (("a", "b"), (1, 2), None),
    (("a", "b", "x"), (1, 2, None), None),
    (("a", "b", "x"), (1, 2, "Missing"), "Missing"),
])
def test_get_keys(keys: Any, expected: Any, default: Any) -> None:
    assert get_keys({"a": 1, "b": 2}, keys, default) == expected


@pytest.mark.parametrize("args, expected", [
    ((('a', 'b', 'c'), False, None), {'a': 1, 'b': 2, 'c': 3}),
    ((('a', 'b', 'z'), True, None), {'a': 1, 'b': 2}),
    ((('a', 'b', 'z'), False, None), {'a': 1, 'b': 2, 'z': None}),
    ((('a', 'b', 'z'), False, 'Missing'), {'a': 1, 'b': 2, 'z': 'Missing'}),
])
def test_dict_subset(args: Any, expected: Any) -> None:
    d = {'a': 1, 'b': 2, 'c': 3}
    assert dict_subset(d, *args) == expected


@pytest.mark.parametrize("data, keys, expected", [
    ({'a': {'b': {'c': 3}}}, 'a', {'b': {'c': 3}}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b', 'c'), 3)
])
def test_get_in_dict(data: Any, keys: Any, expected: Any) -> None:
    assert get_in_dict(data, keys) == expected


@pytest.mark.parametrize("data, keys, value, expected", [
    ({'a': {'b': {'c': 3}}}, 'a', 20, {'a': 20}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b'), 5, {'a': {'b': 5}}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b', 'c'), 5, {'a': {'b': {'c': 5}}})
])
def test_set_in_dict(data: Any, keys: Any, value: Any, expected: Any) -> None:
    set_in_dict(data, keys, value)
    assert data == expected


@pytest.mark.parametrize("args, expected", [
    (([1, 5, 2, 1, 9, 1, 5, 10], None), [1, 5, 2, 9, 10]),
    ((["jack", "joe", "jay", "ian"], len), ["jack", "joe"])
])
def test_dedupe(args: Any, expected: Any) -> None:
    """Tests that dedupe removes duplicates whilst preserving order"""
    assert list(dedupe(*args)) == expected


@pytest.mark.parametrize("args, expected", [
    (({'Homer': 39, 'Marge': 36, 'Bart': 10}, lambda x: x < 20), {'Bart': 10}),
    (({'a': None, 'b': 2, 'c': None},), {'b': 2})
])
def test_prune_dict(args: Any, expected: Any) -> None:
    assert prune_dict(*args) == expected


@pytest.mark.parametrize("args, expected", [
    ((1, [2, 3]), [1, 2, 3]),
    ((2, [3, 4, 5, 6]), [2, 3, 4, 5, 6]),
])
def test_cons(args: Any, expected: Any) -> None:
    assert list(cons(*args)) == expected
