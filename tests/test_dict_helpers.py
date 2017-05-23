from typing import Any

import pytest  # type: ignore

from basic_utils.dict_helpers import (
    dict_subset,
    get_in_dict,
    get_keys,
    prune_dict,
    set_in_dict
)


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


@pytest.mark.parametrize("keys, expected, default", [
    (("a", "b"), (1, 2), None),
    (("a", "b", "x"), (1, 2, None), None),
    (("a", "b", "x"), (1, 2, "Missing"), "Missing"),
])
def test_get_keys(keys: Any, expected: Any, default: Any) -> None:
    assert get_keys({"a": 1, "b": 2}, keys, default) == expected


@pytest.mark.parametrize("args, expected", [
    (({'Homer': 39, 'Marge': 36, 'Bart': 10}, lambda x: x < 20), {'Bart': 10}),
    (({'a': None, 'b': 2, 'c': None},), {'b': 2})
])
def test_prune_dict(args: Any, expected: Any) -> None:
    assert prune_dict(*args) == expected


@pytest.mark.parametrize("data, keys, value, expected", [
    ({'a': {'b': {'c': 3}}}, 'a', 20, {'a': 20}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b'), 5, {'a': {'b': 5}}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b', 'c'), 5, {'a': {'b': {'c': 5}}})
])
def test_set_in_dict(data: Any, keys: Any, value: Any, expected: Any) -> None:
    set_in_dict(data, keys, value)
    assert data == expected
