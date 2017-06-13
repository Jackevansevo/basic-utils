from functools import partial
from operator import eq
from typing import Any

import pytest  # type: ignore

from basic_utils.dict_helpers import (
    filter_keys,
    filter_values,
    get_in_dict,
    get_keys,
    prune_dict,
    set_in_dict
)
from basic_utils.primitives import even


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
    (({'Homer': 39, 'Bart': 10}, lambda x: x < 20), {'Bart': 10}),
    (({'Homer': 39, 'Bart': 10}, partial(eq, 10)), {'Bart': 10}),
    (({'a': 1, 'b': 2, 'c': 3, 'd': 4}, even), {'b': 2, 'd': 4}),
])
def test_filter_values(args: Any, expected: Any) -> None:
    assert filter_values(*args) == expected


@pytest.mark.parametrize("args, expected", [
    (({'Lisa': 8, 'Marge': 36}, lambda x: len(x) > 4), {'Marge': 36}),
    (({'Homer': 39, 'Bart': 10}, partial(eq, 'Bart')), {'Bart': 10}),
])
def test_filter_keys(args: Any, expected: Any) -> None:
    assert filter_keys(*args) == expected


@pytest.mark.parametrize("args, expected", [
    (({'a': None, 'b': 2, 'c': False},), {'b': 2}),
    (({'a': [], 'b': 2, 'c': {}},), {'b': 2})
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
