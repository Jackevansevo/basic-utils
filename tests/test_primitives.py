from typing import Any, Tuple

import pytest  # type: ignore

from basic_utils.primitives import (
    comp,
    complement,
    dec,
    even,
    identity,
    inc,
    odd
)


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


def test_primitives() -> None:
    assert inc(1) == 2
    assert dec(2) == 1
    assert even(2)
    assert not even(1)
    assert odd(1)
    assert not odd(2)
