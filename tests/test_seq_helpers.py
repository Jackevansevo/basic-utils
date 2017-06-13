from typing import Any

import pytest  # type: ignore

from basic_utils.primitives import natural_nums
from basic_utils.seq_helpers import (
    all_equal,
    butlast,
    concat,
    cons,
    dedupe,
    first,
    flatten,
    last,
    nth,
    partial_flatten,
    quantify,
    rest,
    reverse,
    second,
    sorted_index,
    take
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
    ((1, 2, (3, (4,))), (1, 2, 3, 4)),
    (((1,), (2,), (3, 4)), (1, 2, 3, 4))
])
def test_flatten(args: Any, expected: Any) -> None:
    """
    Tests that flatten returns a completely flattened version nested data
    """
    assert flatten(args) == expected


@pytest.mark.parametrize("args, expected", [
    ([[1], [2], [3]], [1, 2, 3]),
    ([[1, 2], [3, 4, 5]], [1, 2, 3, 4, 5]),
    (((1, 2), (3,)), (1, 2, 3)),
])
def test_partial_flatten(args: Any, expected: Any) -> None:
    """
    Tests that partial_flatten returns a partially flattened version data
    """
    assert partial_flatten(args) == expected


@pytest.mark.parametrize("args, expected", [
    (([1, 5, 2, 1, 9, 1, 5, 10], None), [1, 5, 2, 9, 10]),
    ((("jack", "joe", "jay", "ian"), len), ("jack", "joe"))
])
def test_dedupe(args: Any, expected: Any) -> None:
    """Tests that dedupe removes duplicates whilst preserving order"""
    assert dedupe(*args) == expected


@pytest.mark.parametrize("args, expected", [
    ((1, [2, 3]), [1, 2, 3]),
    ((2, [3, 4, 5, 6]), [2, 3, 4, 5, 6]),
])
def test_cons(args: Any, expected: Any) -> None:
    assert list(cons(*args)) == expected


@pytest.mark.parametrize("args, expected", [
    (([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
    (((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6)),
    (({1, 2, 3}, {4, 5, 6}), {1, 2, 3, 4, 5, 6}),
    (([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])
])
def test_concat(args: Any, expected: Any) -> None:
    assert concat(*args) == expected


@pytest.mark.parametrize("args, expected", [
    (([10, 20, 30, 40, 50], 35), 3),
    (([1, 2, 2, 3], 2), 1),
    (([], 5), 0),
])
def test_sorted_index(args: Any, expected: Any) -> None:
    assert sorted_index(*args) == expected


@pytest.mark.parametrize("args, expected", [
    ((2, range(1, 10)), [1, 2]),
    ((5, natural_nums()), [0, 1, 2, 3, 4])
])
def test_take(args: Any, expected: Any) -> None:
    assert take(*args) == expected


@pytest.mark.parametrize("args, expected", [
    (([1, 2, 3], 1), 2),
    ((natural_nums(), 3), 3)
])
def test_nth(args: Any, expected: Any) -> None:
    assert nth(*args) == expected


@pytest.mark.parametrize("args, expected", [
    ([1, 1], True),
    (['a', 'b'], False),
    ([True, []], False),
    ([], True)
])
def test_all_equal(args: Any, expected: Any) -> None:
    assert all_equal(args) == expected


@pytest.mark.parametrize("args, expected", [
    ([True, True, True], 3),
    ([True, False, True], 2),
    ([], 0),
])
def test_quantify(args: Any, expected: Any) -> None:
    assert quantify(args) == expected
