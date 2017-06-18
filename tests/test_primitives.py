from hypothesis import given
from hypothesis.strategies import integers
from typing import Any, Tuple

import pytest  # type: ignore

from basic_utils.primitives import (
    comp,
    complement,
    dec,
    even,
    identity,
    inc,
    natural_nums,
    odd
)
from basic_utils.seq_helpers import take


def test_natural_nums() -> None:
    assert take(3, natural_nums(7)) == [7, 8, 9]
    assert take(5, natural_nums(1, 4)) == [1, 2, 3]
    assert take(2, natural_nums(1, 4)) == [1, 2]


@pytest.mark.parametrize("data", [
    (10), ((10, 20)), (("Homer", "Marge"))
])
def test_identity(data: Tuple[Any]) -> None:
    """Tests that identity returns the same arguments as it was passed"""
    assert identity(data) == data


def test_comp() -> None:
    assert comp(complement, even)(3)
    assert comp(complement, odd)(2)


def test_complement() -> None:
    fn = complement(even)
    assert fn(5)
    fn = complement(lambda x: x.startswith('a'))
    assert fn('grapple')


@given(integers())
def test_inc(i: int) -> None:
    assert inc(i) == i + 1


@given(integers())
def test_dec(i: int) -> None:
    assert dec(i) == i - 1


@given(integers())
def test_odd(i: int) -> None:
    assert odd(i) == bool(i % 2 != 0)


@given(integers())
def test_even(i: int) -> None:
    assert even(i) == bool(i % 2 == 0)
