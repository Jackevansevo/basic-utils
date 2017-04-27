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


@pytest.mark.parametrize("data", [
    ([1, 2, 3]),
    ((1, 2, 3,)),
    (range(1, 4)),
])
def test_first(data):
    """Tests that first returns the first element in a sequence"""
    assert first(data) == 1


@pytest.mark.parametrize("data", [
    ([1, 2, 3]),
    ((1, 2, 3,)),
    (range(1, 4)),
])
def test_last(data):
    """Tests that last returns the last element in a sequence"""
    assert last(data) == 3


@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], [2, 3]),
    ((1, 2, 3), (2, 3)),
    ((range(1, 4)), range(2, 4)),
])
def test_rest(data, expected):
    """Tests that rest returns the remaining elements in a sequence"""
    assert rest(data) == expected


@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], [1, 2]),
    ((1, 2, 3), (1, 2)),
    (range(1, 4), range(1, 3))
])
def test_butlast(data, expected):
    """Tests that butlast returns all but the last element in a sequence"""
    assert butlast(data) == expected


@pytest.mark.parametrize("data, expected", [
    ('hello world', 'dlrow olleh'),
    ([1, 2, 3], [3, 2, 1]),
    ((1, 2, 3), (3, 2, 1)),
    (range(1, 4), range(3, 0, -1)),
])
def test_reverse(data, expected):
    assert reverse(data) == expected


@pytest.mark.parametrize("data, expected", [
    ([[1, [2, [3, [4]]]]], [1, 2, 3, 4]),
    ((1, 2, (3, (4,))), [1, 2, 3, 4]),
    (((1,), (2,), (3, 4)), [1, 2, 3, 4])
])
def test_flatten(data, expected):
    """
    Tests that flatten returns a completely flattened version nested data
    """
    assert list(flatten(data)) == expected


@pytest.mark.parametrize("data, expected", [
    ([[1], [2], [3]], [1, 2, 3]),
    ([[1, 2], [3, 4, 5]], [1, 2, 3, 4, 5]),
    (((1, 2), (3,)), [1, 2, 3]),
])
def test_partial_flatten(data, expected):
    """
    Tests that partial_flatten returns a partially flattened version data
    """
    assert list(partial_flatten(data)) == expected


@pytest.mark.parametrize("keys, expected, default", [
    (("a", "b"), (1, 2), None),
    (("a", "b", "x"), (1, 2, None), None),
    (("a", "b", "x"), (1, 2, "Missing"), "Missing"),
])
def test_get_keys(keys, expected, default):
    assert get_keys({"a": 1, "b": 2}, keys, default) == expected


@pytest.mark.parametrize("keys, expected, prune, default", [
    (('a', 'b', 'c'), {'a': 1, 'b': 2, 'c': 3}, False, None),
    (('a', 'b', 'z'), {'a': 1, 'b': 2}, True, None),
    (('a', 'b', 'z'), {'a': 1, 'b': 2, 'z': None}, False, None),
    (('a', 'b', 'z'), {'a': 1, 'b': 2, 'z': 'Missing'}, False, 'Missing'),
])
def test_dict_subset(keys, expected, prune, default):
    d = {'a': 1, 'b': 2, 'c': 3}
    assert dict_subset(d, keys, prune, default) == expected


@pytest.mark.parametrize("data, keys, expected", [
    ({'a': {'b': {'c': 3}}}, 'a', {'b': {'c': 3}}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b', 'c'), 3)
])
def test_get_in_dict(data, keys, expected):
    assert get_in_dict(data, keys) == expected


@pytest.mark.parametrize("data, keys, value, expected", [
    ({'a': {'b': {'c': 3}}}, 'a', 20, {'a': 20}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b'), 5, {'a': {'b': 5}}),
    ({'a': {'b': {'c': 3}}}, ('a', 'b', 'c'), 5, {'a': {'b': {'c': 5}}})
])
def test_set_in_dict(data, keys, value, expected):
    set_in_dict(data, keys, value)
    assert data == expected


@pytest.mark.parametrize("data, key, expected", [
    ([1, 5, 2, 1, 9, 1, 5, 10], None, [1, 5, 2, 9, 10]),
    (["jack", "joe", "jay", "ian"], len, ["jack", "joe"])
])
def test_dedupe(data, key, expected):
    """Tests that dedupe removes duplicates whilst preserving order"""
    assert list(dedupe(data, key)) == expected


@pytest.mark.parametrize("args, expected", [
    (({'Homer': 39, 'Marge': 36, 'Bart': 10}, lambda x: x < 20), {'Bart': 10}),
    (({'a': None, 'b': 2, 'c': None},), {'b': 2})
])
def test_prune_dict(args, expected):
    assert prune_dict(*args) == expected


@pytest.mark.parametrize("data, expected", [
    ((1, [2, 3]), [1, 2, 3]),
    ((2, [3, 4, 5, 6]), [2, 3, 4, 5, 6]),
])
def test_cons(data, expected):
    assert list(cons(*data)) == expected
